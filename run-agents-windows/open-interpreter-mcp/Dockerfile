# Use official Python slim image
FROM ubuntu:22.04
# FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system deps (for Ollama TLS, if needed)
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    nano \
    curl 
    # --no-install-recommends && \
    # rm -rf /var/lib/apt/lists/*

# RUN python3 -m pip config set global.break-system-packages true

# Copy and install Python dependencies
RUN pip install fastapi uvicorn open-interpreter fastmcp python-dotenv

# Copy application code
COPY server.py .

# Expose port for API
EXPOSE 8000

# Entrypoint: start Uvicorn server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
