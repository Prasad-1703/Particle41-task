**SimpleTimeService**
**Project Overview**

SimpleTimeService is a minimalist web microservice that provides the current timestamp and the IP address of the visitor. The application is built using Python and the Flask framework, containerized using Docker, and configured to run as a non-root user.

Response Structure:

When accessing the root (/) endpoint, the service returns a JSON response with the following structure:

{
  "timestamp": <current date and time>,
  "ip": <IP address of the visitor>
}

**Prerequisites**

Docker installed: Install Docker

Optional (for local testing without Docker)

Python 3.9+ installed: Install Python

Instructions to Build and Run the Application

1. Clone the Repository

  git clone https://github.com/Prasad-1703/Particle41-task.git

  cd SimpleTimeService

2. Build the Docker Image

  docker build -t simpletimeservice .

3. Run the Docker Container

  docker run -itd -p 8080:8080 simpletimeservice

4. Access the Application

  Open a web browser or use curl to test the service:

  http://localhost:8080/

Sample Response:

{
  "timestamp": "2025-01-31 15:25:10",
  "ip": "127.0.0.1"
}

Docker Best Practices Followed

Non-root User: The application runs as a non-root user (appuser) inside the container.

Small Image: A minimal base image (python:3.9-slim) is used.

Environment Variables: Python buffering disabled for better logging (PYTHONUNBUFFERED=1).

Publish to Docker Hub

1. Login to Docker Hub

docker login

2. Tag the Image

docker tag simpletimeservice your_dockerhub_username/simpletimeservice:latest

3. Push the Image

docker push your_dockerhub_username/simpletimeservice:latest

Local Testing Without Docker (Optional)

pip install flask
python app.py

Access the service at:

http://localhost:8080/

Project Structure

Task1-SimpleTimeService
├── Dockerfile
├── app.py
└── README.md

