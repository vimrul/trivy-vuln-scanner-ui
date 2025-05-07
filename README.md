# 🛡️ Trivy Vulnerability Scanner Dashboard (FastAPI + PostgreSQL)

A self-hosted web API built with **FastAPI**, **PostgreSQL**, and **Docker**, designed to manage Docker image vulnerability scan results using **Trivy**. Includes full authentication (JWT-based), user-role access, project management, image tracking, and vulnerability reporting.

---

## 📦 Features

- 🔐 JWT-based authentication
- 👥 Role-based user management (`admin`, `developer`)
- 📁 Project creation & image association
- 📊 Upload and view Trivy scan results per image
- 📄 Built with FastAPI, SQLAlchemy, Alembic
- 🐳 Dockerized setup with PostgreSQL backend

---

## ⚙️ Docker Setup

### 1. 📁 Directory Structure

Assumes the following structure:

```
.
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
```

---

### 2. 🐳 Docker Compose File

`docker-compose.yml` in the project root:

```yaml
version: '3.8'

services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: vuln_dashboard
    volumes:
      - pgdata:/var/lib/postgresql/data

  backend:
    build: ./backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    environment:
      DATABASE_URL: postgresql://dev:devpass@db:5432/vuln_dashboard
      SECRET_KEY: supersecretkey
    volumes:
      - ./backend/app:/app/app
      - ./backend/alembic:/app/alembic
    ports:
      - "9001:8000"
    depends_on:
      - db

volumes:
  pgdata:
```

---

### 3. 🚀 Start the App

```bash
docker compose up --build
```

---

## 🧪 Testing the API via `curl`

---

### ✅ Login as Admin

```bash
curl -X POST http://localhost:9001/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@admin.com&password=password123"
```

Export the token for reuse:

```bash
export TOKEN="your_access_token_here"
```

---

### 👤 Create Developer User

```bash
curl -X POST http://localhost:9001/users/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "email": "dev1@example.com",
    "password": "devpass",
    "role": "developer"
  }'
```

---

### 🏗️ Create Project

```bash
curl -X POST http://localhost:9001/projects/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "name": "MyProject",
    "description": "Test project for Trivy scans"
  }'
```

---

### ➕ Add Developer to Project

```bash
curl -X POST "http://localhost:9001/projects/1/members?user_id=2" \
  -H "Authorization: Bearer $TOKEN"
```

---

### 📤 Upload Trivy Report

Prepare `sample-report.json` and run:

```bash
curl -X POST http://localhost:9001/reports/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data @sample-report.json
```

---

### 📸 View Image Scan Records

```bash
curl -X GET http://localhost:9001/projects/1/images/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## 🔑 Default Admin Credentials

- **Email:** `admin@admin.com`
- **Password:** `password123`

---

## 🛠️ Notes

- To persist users/projects between runs, avoid deleting `pgdata` volume.
- To reset DB, stop containers and remove volumes:

```bash
docker compose down -v
```

---

## 📚 License

MIT License

---

## 💬 Author

Built with ❤️ by [Imrul Hasan]