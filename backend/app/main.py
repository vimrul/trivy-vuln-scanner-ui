# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your existing modules/routers
from app.api import auth, users, projects, images, reports
from app import crud, schemas
from app.database import SessionLocal

app = FastAPI(title="Vuln Dashboard API")

# -------------------------------------------------------------------------------------------------------------------
# 1) Attach CORS middleware here, BEFORE including any routers.
#    We set allow_origins=["*"] to permit requests from any host.
#    In production you may want to lock this down to specific domains,
#    but for now “allow all” is what you requested.
# -------------------------------------------------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow all origins
    allow_credentials=True,       # Allow cookies, Authorization headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],          # Allow all request headers (Content-Type, Authorization, etc.)
)


# -------------------------------------------------------------------------------------------------------------------
# 2) On startup, seed a default admin user if it does not yet exist.
# -------------------------------------------------------------------------------------------------------------------
@app.on_event("startup")
def seed_default_admin():
    db = SessionLocal()
    admin_email = "admin@admin.com"
    admin_password = "password123"
    existing = crud.get_user_by_email(db, admin_email)
    if not existing:
        crud.create_user(
            db,
            schemas.UserCreate(
                email=admin_email,
                password=admin_password,
                role="admin"
            )
        )
    db.close()


# -------------------------------------------------------------------------------------------------------------------
# 3) Include your routers (auth, users, projects, etc.)
# -------------------------------------------------------------------------------------------------------------------
app.include_router(auth.router,      prefix="/auth",    tags=["auth"])
app.include_router(users.router,     prefix="/users",   tags=["users"])
app.include_router(projects.router,  prefix="/projects",tags=["projects"])
app.include_router(
    images.router,
    prefix="/projects/{project_id}/images",
    tags=["images"]
)
app.include_router(reports.router,   prefix="/reports",  tags=["reports"])
