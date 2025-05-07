from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, models
from app.dependencies import get_db, get_current_active_user, get_current_admin_user

router = APIRouter()

@router.post("/", response_model=schemas.Project, status_code=status.HTTP_201_CREATED)
def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    # Admin creates a project
    return crud.create_project(db, project_in, current_user.id)

@router.get("/", response_model=List[schemas.Project])
def list_projects(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    # Admin sees all, developers see only their projects
    if current_user.role == "admin":
        return crud.get_projects(db)
    return crud.get_user_projects(db, current_user.id)

@router.post("/{project_id}/members", response_model=schemas.User)
def add_member(
    project_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    # Admin assigns a developer to a project
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    member = crud.add_project_member(db, project_id, user_id)
    return crud.get_user_by_id(db, user_id)