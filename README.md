**Project Overview**
This repository contains two tasks related to containerization, cloud infrastructure, and Terraform. These tasks are organized into separate folders, each representing a different challenge:

Task 1 - Minimalist Application Development / Docker / Kubernetes
In this task, we create a simple microservice called SimpleTimeService, which returns a JSON response containing the current timestamp and the visitor's IP address.

Key components of this task:

Microservice Development: A web server that provides a JSON response with the current date and time along with the IP address of the visitor.
Dockerization: The microservice is containerized using Docker and configured to run as a non-root user in the container.
Image Publishing: The Docker image is pushed to a public container registry (e.g., DockerHub), making it accessible to others.
Code Repository: All code, including the Dockerfile, source code, and configuration files, are available here.
For detailed instructions on how to build and run the SimpleTimeService application, please refer to the Task 1 README.

Task 2 - Terraform and Cloud Infrastructure
This task involves creating the infrastructure required to host your containerized application using Terraform in AWS (or an equivalent cloud platform). The infrastructure includes:

VPC Creation: Setting up a VPC with two public and two private subnets.
ECS/EKS Cluster: Deploying a containerized service within a cluster (ECS/EKS) in the private subnets.
Load Balancer: A load balancer deployed in public subnets to handle traffic and route it to the containerized service.
Cloud Resources Configuration: Includes security groups, IAM roles, and network configuration.
You can also choose to implement a serverless solution using Lambda, API Gateway, and appropriate subnet associations.

For more detailed instructions on setting up and deploying the infrastructure, please refer to the Task 2 README.

Repository Structure
task1/ - Contains the code, Dockerfile, and configurations for Task 1 (Minimalist Application).
task2/ - Contains the Terraform code and cloud infrastructure configurations for Task 2 (Cloud Infrastructure and Container Hosting).
Notes
Task 1 involves developing a simple application and containerizing it.
Task 2 involves automating cloud infrastructure deployment with Terraform to host the application.
Both tasks involve using cloud technologies and containerization best practices.


# Project Overview

This repository contains two tasks related to containerization, cloud infrastructure, and Terraform. 

<h2>Task 1: SimpleTimeService</h2>
Task 1 focuses on creating a simple microservice...

<h3>Task 2: Terraform Cloud Infrastructure</h3>
In Task 2, we set up the cloud infrastructure using Terraform.
