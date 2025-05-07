from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Any

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None

class UserCreate(BaseModel):
    email: str
    password: str
    role: str

class User(BaseModel):
    id: int
    email: str
    role: str
    is_active: bool

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_by: int
    created_at: datetime
    members: List[User] = []

    class Config:
        orm_mode = True

class ImageBase(BaseModel):
    name: str
    tag: str

class ImageCreate(ImageBase):
    project_id: int

class Image(ImageBase):
    id: int
    project_id: int
    last_scanned_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class Vulnerability(BaseModel):
    id: int
    vuln_id: str
    pkg_name: str
    severity: str
    fixed_version: Optional[str] = None
    type: str

    class Config:
        orm_mode = True

class ScanReport(BaseModel):
    id: int
    image_id: int
    scan_timestamp: datetime
    total_vulns: int
    raw_report: Any
    vulnerabilities: List[Vulnerability] = []

    class Config:
        orm_mode = True