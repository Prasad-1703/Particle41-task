**Task 2 - Terraform and Cloud: Container Hosting Infrastructure**\

This Folder contains the Terraform code to create infrastructure in AWS (or equivalent) for hosting a containerized application. The infrastructure setup can be either server-based or serverless. The infrastructure includes components like VPC, ECS/EKS, subnets, load balancers, and other necessary resources.

Table of Contents
Overview
Infrastructure
Server-based Setup
Getting Started
Prerequisites
Usage

**Overview**

This project sets up the necessary infrastructure to host a containerized application in the cloud using Terraform. Depending on the preference, either a server-based setup (using ECS/EKS) or a serverless setup (using Lambda) is created, with resources like VPC, subnets, and load balancers deployed accordingly.

**Infrastructure**

**Server-based Setup**

The infrastructure will be created as follows:

VPC with 2 public and 2 private subnets.

ECS/EKS cluster deployed within the VPC.

ECS/EKS task/service running the container on private subnets.

Load Balancer deployed on public subnets to offer the service.

**Getting Started**

To get started with this project, follow these steps:

Clone this repository:

git clone https://github.com/yourusername/terraform-container-infrastructure.git

cd terraform-container-infrastructure

Initialize Terraform to download the necessary providers:

  1.terraform init

Review the Terraform plan to ensure the infrastructure is set up as desired:

  2.terraform plan

Apply the Terraform configuration to create the infrastructure:

  3.terraform apply

To destroy the resources (optional), run:

  4.terraform destroy

**Prerequisites**

Before running the Terraform code, make sure you have the following prerequisites:

Terraform installed on your machine (preferably the latest stable version).
AWS CLI configured with appropriate credentials.
Access to a public Git repository (e.g., GitHub, GitLab) for pushing the code.
Usage
After running terraform apply, your containerized application will be accessible based on the setup you have chosen (either ECS/EKS for server-based or Lambda for serverless). The infrastructure will include a load balancer (in the case of server-based) or an API Gateway (for serverless) that will trigger your container function.

To modify the container image or other settings, edit the relevant parts in the container_definitions.json or equivalent files and re-apply the Terraform plan.
