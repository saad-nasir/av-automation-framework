# Use the official Python image as the base
FROM python:3.8-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file from the project root into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY microservices ./microservices

# Expose the port that the service will run on
EXPOSE 5002

# Command to run the service
CMD ["python", "microservices/product_catalog_service/product_catalog_service.py"]