# Project Overview

This repository contains two tasks related to containerization, cloud infrastructure, and Terraform.

<h2>Task 1: SimpleTimeService</h2>

Task 1 focuses on creating a simple microservice in any programming language of your choice, which returns the current date and time in JSON format along with the visitor's IP address.

- **Technologies Used**: Docker, Node.js (or any preferred language)
- **Objective**: Create a web server, dockerize the application, and publish it to a container registry.
- **Containerization**: Dockerfile configured to run as a non-root user and build the container image.
- **GitHub Repository**: [SimpleTimeService](https://github.com/Prasad-1703/Particle41-task/blob/8beab3b8fa714862719648d55aa9664ec6623834/Task1-SimpleTimeService/README.md)

<h2>Task 2: Terraform Cloud Infrastructure</h2>

In Task 2, we set up the cloud infrastructure using Terraform, which hosts the previously created containerized application on AWS (or equivalent).

- **Technologies Used**: Terraform, AWS (or equivalent cloud provider)
- **Objective**: Create a VPC with subnets, deploy ECS service (or equivalent), and expose the service using a load balancer.
- **GitHub Repository**: [Terraform Infrastructure](https://github.com/Prasad-1703/Particle41-task/blob/8beab3b8fa714862719648d55aa9664ec6623834/Task2-terraform/Readme.md)

# Repository Structure

- **task1/** - Contains the code, Dockerfile, and configurations for **Task 1: Minimalist Application Development**.
- **task2/** - Contains the Terraform code and cloud infrastructure configurations for **Task 2: Cloud Infrastructure and Container Hosting**.

# Notes

- **Task 1** involves developing a simple microservice and containerizing it using Docker.
- **Task 2** involves automating the deployment of cloud infrastructure with Terraform to host the containerized application.
- Both tasks leverage cloud technologies and containerization best practices for efficient application deployment and management.
