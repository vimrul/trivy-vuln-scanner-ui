from fastapi import FastAPI
from app.api import auth, users, projects, images, reports

app = FastAPI(title="Vuln Dashboard API")

app.include_router(auth.router,    prefix="/auth",    tags=["auth"])
app.include_router(users.router,   prefix="/users",   tags=["users"])
app.include_router(projects.router,prefix="/projects",tags=["projects"])
app.include_router(images.router,  prefix="/projects/{project_id}/images", tags=["images"])
app.include_router(reports.router, prefix="/reports",   tags=["reports"])