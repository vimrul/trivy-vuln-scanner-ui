FROM python:3.10-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy environment file for BaseSettings
COPY .env .

# Copy application code and migrations
COPY app ./app
COPY alembic ./alembic

# Expose port and launch
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]