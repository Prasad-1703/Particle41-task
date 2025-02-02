# **SimpleTimeService**

## **Project Overview**

**SimpleTimeService** is a minimalist web microservice that provides the current timestamp and the IP address of the visitor. The application is built using Python and the Flask framework, containerized using Docker, and configured to run as a non-root user.

### **Response Structure:**

When accessing the root (/) endpoint, the service returns a JSON response with the following structure:

json
{
  "timestamp": "<current date and time>",
  "ip": "<IP address of the visitor>"
}



**# Prerequisites**
Docker installed: Install Docker

Optional (for local testing without Docker):

Python 3.9+ installed: Install Python

Instructions to Build and Run the Application
Clone the Repository:

git clone https://github.com/Prasad-1703/Particle41-task.git

cd SimpleTimeService

Build the Docker Image:

docker build -t simpletimeservice .

Run the Docker Container:

docker run -itd -p 8080:8080 simpletimeservice

Access the Application:

Open a web browser or use curl to test the service:

http://localhost:8080/

Sample Response:

json
Copy
Edit
{
  "timestamp": "2025-01-31 15:25:10",
  "ip": "127.0.0.1"
}

Docker Best Practices Followed

Non-root User: The application runs as a non-root user (appuser) inside the container.
Small Image: A minimal base image (python:3.9-slim) is used to reduce the image size.
Environment Variables: Python buffering is disabled for better logging (PYTHONUNBUFFERED=1).
Publish to Docker Hub
Login to Docker Hub:

docker login

Tag the Image:

docker tag simpletimeservice prasad1703/simpletimeservice:latest

Push the Image:

docker push prasad1703/simpletimeservice:latest

Local Testing Without Docker (Optional)

Install Flask:

pip install flask

Run the application:

python app.py

Access the service at:

http://localhost:8080/

Project Structure

Task1-SimpleTimeService
├── Dockerfile
├── app.py
└── README.md
