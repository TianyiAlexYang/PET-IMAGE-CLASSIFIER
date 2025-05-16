FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies and clean up to reduce image size
RUN apt-get update && \
    apt-get install -y build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies using requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port for the application
EXPOSE 8080

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
