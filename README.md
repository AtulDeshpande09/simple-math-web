# Simple Math Web

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0%2B-lightgrey)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight Flask-based web application that performs basic arithmetic operations. This project serves as a practical demonstration and learning resource for containerizing Python applications using Docker.

## Features

- Finds solution of linear eq in two variables and quadratic equations
- Fully containerized deployment using Docker
- Lightweight and easy to extend

## Tech Stack

- **Backend:** Python, Flask
- **Containerization:** Docker

## Project Structure

```text
simple-math-web/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build instructions
└── .dockerignore       # Files to exclude from Docker build
```

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.9 or higher
- Docker (for containerized deployment)

## Running Locally

To run the application natively on your machine:

1. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Start the application:

```bash
python app.py
```

The application will be available at: [http://localhost:5000](http://localhost:5000)


## Docker Usage

This project is designed to demonstrate Docker workflows and container management.

### Build the Docker Image

```bash
docker build -t simple-math-web .
```

### Run the Container

```bash
docker run -d \
  --name math-container \
  -p 5000:5000 \
  simple-math-web
```

### View Logs

```bash
docker logs math-container
```

### Stop and Remove Container

```bash
docker stop math-container
docker rm math-container
```

## Docker Hub

You can also pull the pre-built image directly from Docker Hub:

```bash
docker pull atuldeshpande09/simple-math-web:v1
```

Run the pulled image:

```bash
docker run -d -p 5000:5000 atuldeshpande09/simple-math-web:v1
```

## Learning Goals

This project was created as a demo to cover the following Docker and deployment concepts:

- Building Docker images from a Dockerfile
- Managing Docker containers (run, stop, logs, remove)
- Understanding `.dockerignore`
- Port mapping between host and container
- Container lifecycle management
- Publishing and pulling images from Docker Hub

## License

This project is open-source and available under the [MIT License](LICENSE).
```
