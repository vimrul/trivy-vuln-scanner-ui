from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Project
def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def create_project(db: Session, project: schemas.ProjectCreate, user_id: int):
    db_proj = models.Project(**project.dict(), created_by=user_id)
    db.add(db_proj)
    db.commit()
    db.refresh(db_proj)
    return db_proj

def add_project_member(db: Session, project_id: int, user_id: int):
    pm = models.ProjectMember(project_id=project_id, user_id=user_id)
    db.add(pm)
    db.commit()
    return pm

# Image & Reports
def get_image(db: Session, project_id: int, name: str, tag: str):
    return db.query(models.Image).filter(
        models.Image.project_id==project_id,
        models.Image.name==name,
        models.Image.tag==tag
    ).first()

def create_image(db: Session, image: schemas.ImageCreate):
    img = models.Image(**image.dict())
    db.add(img)
    db.commit()
    db.refresh(img)
    return img

def create_scan_report(db: Session, image_id: int, total_vulns: int, raw: dict):
    report = models.ScanReport(image_id=image_id, total_vulns=total_vulns, raw_report=raw)
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

def create_vulnerabilities(db: Session, report_id: int, vulns: list):
    objs = []
    for v in vulns:
        obj = models.Vulnerability(
            report_id=report_id,
            vuln_id=v.get("VulnerabilityID"),
            pkg_name=v.get("PkgName"),
            severity=v.get("Severity"),
            fixed_version=v.get("FixedVersion"),
            type=v.get("Type", "application")
        )
        objs.append(obj)
    db.bulk_save_objects(objs)
    db.commit()
    return objs