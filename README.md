# FastAPI S3 File Management with Docker Compose

This project demonstrates how to integrate **FastAPI** with an **S3-compatible object storage service** for file management. The setup uses **MinIO** as the S3-compatible storage service and runs everything in Docker Compose for easy deployment.

## Features
- Upload files to S3.
- Download files from S3.
- List files in S3 buckets.
- Delete files from S3.

## Technologies Used
- **FastAPI**: Web framework for building APIs.
- **MinIO**: Self-hosted S3-compatible object storage.
- **Docker Compose**: Container orchestration for easy deployment.
- **Boto3**: AWS SDK for Python, used for S3 interaction.

## Prerequisites
- Docker and Docker Compose installed on your machine.
- Basic understanding of Python and FastAPI.

## Setup and Usage

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Configure Environment Variables
Create a `.env` file in the project root directory and set the variables respectively to the .env.example file

### 3. Run the Project
Start the services using Docker Compose:
```bash
docker-compose up --build
```

### 4. Access the Services
- **MinIO Console**: [http://localhost:9001](http://localhost:9001)  
  Use the `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` to log in.
- **FastAPI Swagger UI**: [http://localhost:8090/docs](http://localhost:8090/docs)

## Notes
- Make sure to configure MinIO with the correct credentials (`MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`).
- You can switch to AWS S3 by modifying the S3 endpoint in the configuration.

## References
- [Guide to S3 File Management - FastAPI and S3 Service in Docker Compose](https://medium.com/@gnetkov/guide-to-s3-file-management-fastapi-and-s3-service-in-docker-compose-1d26900f67cc)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MinIO Documentation](https://min.io/docs/)
