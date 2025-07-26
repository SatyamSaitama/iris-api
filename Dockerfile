# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn[standard] scikit-learn pandas joblib

# Expose port
EXPOSE 8000

CMD ["uvicorn", "iris_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
# Start FastAPI app
