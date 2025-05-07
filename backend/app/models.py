from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # 'admin' or 'developer'
    is_active = Column(Boolean, default=True)

    projects = relationship('ProjectMember', back_populates='user')

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship('User')
    members = relationship('ProjectMember', back_populates='project')
    images = relationship('Image', back_populates='project')

class ProjectMember(Base):
    __tablename__ = 'project_members'
    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    project = relationship('Project', back_populates='members')
    user = relationship('User', back_populates='projects')

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    name = Column(String, index=True, nullable=False)
    tag = Column(String, nullable=False)
    last_scanned_at = Column(DateTime, default=None)

    project = relationship('Project', back_populates='images')
    scan_reports = relationship('ScanReport', back_populates='image')

class ScanReport(Base):
    __tablename__ = 'scan_reports'
    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey('images.id'))
    scan_timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    total_vulns = Column(Integer)
    raw_report = Column(JSON)

    image = relationship('Image', back_populates='scan_reports')
    vulnerabilities = relationship('Vulnerability', back_populates='report')

class Vulnerability(Base):
    __tablename__ = 'vulnerabilities'
    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(Integer, ForeignKey('scan_reports.id'))
    vuln_id = Column(String)
    pkg_name = Column(String)
    severity = Column(String)
    fixed_version = Column(String)
    type = Column(String)  # 'base' or 'application'

    report = relationship('ScanReport', back_populates='vulnerabilities')