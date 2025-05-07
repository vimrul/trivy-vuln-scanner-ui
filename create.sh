#!/usr/bin/env bash
set -euo pipefail

ROOT="vuln-dashboard"

# 1. Create all directories
declare -a DIRS=(
  "$ROOT/scanner/config"
  "$ROOT/scanner/examples"
  "$ROOT/backend/alembic/versions"
  "$ROOT/backend/app/api"
  "$ROOT/backend/tests"
  "$ROOT/frontend/public"
  "$ROOT/frontend/src/routes"
  "$ROOT/frontend/src/components"
  "$ROOT/frontend/src/services"
  "$ROOT/frontend/src/context"
  "$ROOT/frontend/src/types"
)

for d in "${DIRS[@]}"; do
  mkdir -p "$d"
done

# 2. Create root-level files
declare -a ROOT_FILES=(
  "$ROOT/README.md"
  "$ROOT/.gitignore"
  "$ROOT/docker-compose.yaml"
)

for f in "${ROOT_FILES[@]}"; do
  : > "$f"
done

# 3. Scanner files
declare -a SCANNER_FILES=(
  "$ROOT/scanner/trivy_scan.sh"
  "$ROOT/scanner/config/trivy.yaml"
  "$ROOT/scanner/examples/sample-report.json"
)

for f in "${SCANNER_FILES[@]}"; do
  : > "$f"
done
chmod +x "$ROOT/scanner/trivy_scan.sh"

# 4. Backend files
declare -a BACKEND_FILES=(
  "$ROOT/backend/Dockerfile"
  "$ROOT/backend/requirements.txt"
  "$ROOT/backend/alembic/env.py"
  "$ROOT/backend/alembic/script.py.mako"
  "$ROOT/backend/app/main.py"
  "$ROOT/backend/app/config.py"
  "$ROOT/backend/app/database.py"
  "$ROOT/backend/app/models.py"
  "$ROOT/backend/app/schemas.py"
  "$ROOT/backend/app/crud.py"
  "$ROOT/backend/app/dependencies.py"
  "$ROOT/backend/app/api/auth.py"
  "$ROOT/backend/app/api/users.py"
  "$ROOT/backend/app/api/projects.py"
  "$ROOT/backend/app/api/images.py"
  "$ROOT/backend/app/api/reports.py"
  "$ROOT/backend/tests/conftest.py"
  "$ROOT/backend/tests/test_auth.py"
  "$ROOT/backend/tests/test_projects.py"
  "$ROOT/backend/tests/test_reports.py"
)

for f in "${BACKEND_FILES[@]}"; do
  : > "$f"
done

# 5. Frontend files
declare -a FRONTEND_FILES=(
  "$ROOT/frontend/Dockerfile"
  "$ROOT/frontend/package.json"
  "$ROOT/frontend/tsconfig.json"
  "$ROOT/frontend/tailwind.config.js"
  "$ROOT/frontend/public/index.html"
  "$ROOT/frontend/src/index.tsx"
  "$ROOT/frontend/src/App.tsx"
  "$ROOT/frontend/src/routes/LoginPage.tsx"
  "$ROOT/frontend/src/routes/ProjectList.tsx"
  "$ROOT/frontend/src/routes/ProjectDetail.tsx"
  "$ROOT/frontend/src/routes/HistoryPage.tsx"
  "$ROOT/frontend/src/components/Navbar.tsx"
  "$ROOT/frontend/src/components/ProjectCard.tsx"
  "$ROOT/frontend/src/components/ImageTable.tsx"
  "$ROOT/frontend/src/components/VulnChart.tsx"
  "$ROOT/frontend/src/services/authService.ts"
  "$ROOT/frontend/src/services/projectService.ts"
  "$ROOT/frontend/src/services/reportService.ts"
  "$ROOT/frontend/src/context/AuthContext.tsx"
  "$ROOT/frontend/src/types/index.ts"
)

for f in "${FRONTEND_FILES[@]}"; do
  : > "$f"
done

echo "✅ vuln-dashboard structure created."
