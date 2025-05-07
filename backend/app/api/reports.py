from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Any, Dict, List
from app import schemas, crud, models
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.ScanReport, status_code=status.HTTP_201_CREATED)
def ingest_report(
    report: Dict[str, Any],
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Extract image & project details from payload
    project_id = report.get("ProjectId")
    image_name = report.get("ArtifactName")
    image_tag = report.get("ArtifactTag", "")
    if not project_id or not image_name:
        raise HTTPException(status_code=400, detail="Missing ProjectId or ArtifactName in payload")

    # Upsert Image record
    db_image = crud.get_image(db, project_id, image_name, image_tag)
    if not db_image:
        db_image = crud.create_image(
            db,
            schemas.ImageCreate(project_id=project_id, name=image_name, tag=image_tag)
        )
    # Update scan timestamp
    db_image.last_scanned_at = datetime.utcnow()
    db.add(db_image)
    db.commit()

    # Save ScanReport
    results: List[Dict[str, Any]] = report.get("Results", [])
    total_vulns = sum(len(r.get("Vulnerabilities", [])) for r in results)
    scan_report = crud.create_scan_report(db, db_image.id, total_vulns, report)

    # Bulk insert vulnerabilities
    vulnerabilities = []
    for r in results:
        for v in r.get("Vulnerabilities", []):
            vulnerabilities.append(v)
    crud.create_vulnerabilities(db, scan_report.id, vulnerabilities)

    return scan_report