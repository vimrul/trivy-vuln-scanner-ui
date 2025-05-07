from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app import schemas, crud, models
from app.dependencies import get_db, get_current_active_user

router = APIRouter()

@router.get("/", response_model=List[schemas.Image])
def list_images(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    # Verify project exists
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    # If developer, ensure membership
    if current_user.role != "admin":
        member_ids = [m.user_id for m in project.members]
        if current_user.id not in member_ids:
            raise HTTPException(status_code=403, detail="Not a project member")
    return crud.get_images_by_project(db, project_id)

@router.get("/{image_id}/vulns", response_model=List[schemas.Vulnerability])
def get_image_vulns(
    project_id: int,
    image_id: int,
    type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    # Verify image exists in project
    image = crud.get_image_by_id(db, image_id)
    if not image or image.project_id != project_id:
        raise HTTPException(status_code=404, detail="Image not found in project")
    # If developer, ensure membership
    if current_user.role != "admin":
        member_ids = [m.user_id for m in image.project.members]
        if current_user.id not in member_ids:
            raise HTTPException(status_code=403, detail="Not a project member")
    return crud.get_vulnerabilities(db, image_id, type)