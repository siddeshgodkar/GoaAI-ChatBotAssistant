# Use lightweight Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend app code (only app/ folder and other files like main.py, api/, etc.)
COPY app/ /app/app

# Expose backend port
EXPOSE 8000

# Start FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
