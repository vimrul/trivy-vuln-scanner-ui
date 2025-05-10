# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy env file and app code
COPY .env .
COPY app ./app
COPY alembic.ini .
COPY alembic ./alembic

# Expose FastAPI port
EXPOSE 8000

# Run Alembic migration, then start the app
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
