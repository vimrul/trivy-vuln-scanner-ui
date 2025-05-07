from typing import List, Optional
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password verification
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# User operations
def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session) -> List[models.User]:
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_pw = pwd_context.hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_pw,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Project operations
def get_project(db: Session, project_id: int) -> Optional[models.Project]:
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def get_projects(db: Session) -> List[models.Project]:
    return db.query(models.Project).all()

def get_user_projects(db: Session, user_id: int) -> List[models.Project]:
    return (
        db.query(models.Project)
        .join(models.ProjectMember)
        .filter(models.ProjectMember.user_id == user_id)
        .all()
    )

def create_project(db: Session, project: schemas.ProjectCreate, user_id: int) -> models.Project:
    db_proj = models.Project(
        **project.dict(),
        created_by=user_id
    )
    db.add(db_proj)
    db.commit()
    db.refresh(db_proj)
    return db_proj

def add_project_member(db: Session, project_id: int, user_id: int) -> models.ProjectMember:
    pm = models.ProjectMember(project_id=project_id, user_id=user_id)
    db.add(pm)
    db.commit()
    return pm

# Image & Report operations
def get_image(db: Session, project_id: int, name: str, tag: str) -> Optional[models.Image]:
    return (
        db.query(models.Image)
        .filter(
            models.Image.project_id == project_id,
            models.Image.name == name,
            models.Image.tag == tag
        )
        .first()
    )

def create_image(db: Session, image: schemas.ImageCreate) -> models.Image:
    img = models.Image(**image.dict())
    db.add(img)
    db.commit()
    db.refresh(img)
    return img

def create_scan_report(db: Session, image_id: int, total_vulns: int, raw: dict) -> models.ScanReport:
    report = models.ScanReport(
        image_id=image_id,
        total_vulns=total_vulns,
        raw_report=raw
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

def create_vulnerabilities(db: Session, report_id: int, vulns: List[dict]) -> List[models.Vulnerability]:
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