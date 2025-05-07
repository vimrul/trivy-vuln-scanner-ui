# backend/app/main.py

from fastapi import FastAPI
from app.api import auth, users, projects, images, reports
from app import crud, schemas
from app.database import SessionLocal

app = FastAPI(title="Vuln Dashboard API")

@app.on_event("startup")
def seed_default_admin():
    db = SessionLocal()
    admin_email = "admin@admin.com"
    admin_password = "password123"
    # Check if the default admin already exists
    existing = crud.get_user_by_email(db, admin_email)
    if not existing:
        # Create the default admin user
        crud.create_user(
            db,
            schemas.UserCreate(
                email=admin_email,
                password=admin_password,
                role="admin"
            )
        )
    db.close()

# Routers
app.include_router(auth.router,     prefix="/auth",    tags=["auth"])
app.include_router(users.router,    prefix="/users",   tags=["users"])
app.include_router(projects.router, prefix="/projects",tags=["projects"])
app.include_router(images.router,   prefix="/projects/{project_id}/images", tags=["images"])
app.include_router(reports.router,  prefix="/reports",  tags=["reports"])
