# Local LLM Hosting with Docker
This repository provides a simple and scalable way to host Large Language Models (LLMs) locally using Docker. It supports both vLLM and Ollama, and includes scripts for easy deployment, management, and interaction with your models.

## Table of Contents- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites- Docker installed (version20.10 or higher)
- NVIDIA Container Toolkit (for GPU support)
- Sufficient disk space for model files- Optional: GPU with CUDA support## Quick Start1. Clone the repository:
```git clone https://github.com/yourusername/local-llm-hosting-docker.git cd local-llm-hosting-docker ```
2. Install prerequisites (see prerequisite.md).
3. Build and run the Docker container:
```docker-compose up --build ```
4. Access the API at http://localhost:8000 (or the port specified in your config).

## Repository Structure- Dockerfile: Base Docker image for running LLMs.
- docker-compose.yaml: Docker Compose configuration for multi-container setups.
- server.py: Main server script for handling model inference.
- client.py: Example client for interacting with the API.
- gptq_marlin.py: Model quantization and optimization script.
- run.sh: Script to start the service.
- run.bat: Windows batch script to start the service.
- stop.sh: Script to stop the service.
- stop.bat: Windows batch script to stop the service.
- prerequisite.md: Guide for installing required tools.

## Usage- Run `docker-compose up --build` to start the container.
- Use `client.py` or `curl` to interact with the API.
- Models can be managed via the scripts provided.

## Scripts Overview- run.sh/run.bat: Starts the Docker service.
- stop.sh/stop.bat: Stops the Docker service.
- server.py: Handles incoming requests and model inference.
- client.py: Example script to send requests to the API.
- gptq_marlin.py: Script for quantizing and optimizing models.

## Configuration- Edit docker-compose.yaml to change ports or add volumes.
- Modify server.py for custom model loading or API endpoints.
- Update run.sh/run.bat for environment-specific setup.

## Troubleshooting- If the model does not load, check the model name and path.
- If the GPU is not detected, ensure NVIDIA Container Toolkit is installed.
- For permission errors, run Docker commands with sudo or add your user to the docker group.
- If the API is unreachable, check the port mapping in docker-compose.yaml.

## LicenseThis project is licensed under the MIT License. See LICENSE for details.
