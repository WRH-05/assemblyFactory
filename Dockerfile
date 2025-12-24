FROM python:3.11-slim

WORKDIR /app

# Copy Python service files
COPY *.py .

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (will be overridden by docker-compose)
EXPOSE 8000

# Default command (will be overridden by docker-compose)
CMD ["uvicorn", "design_service:app", "--host", "0.0.0.0", "--port", "8001"]
