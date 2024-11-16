# Use an official Python image as the base
FROM python:3.8-slim

# Add this after FROM
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*
# Set the working directory
WORKDIR /app

# Copy only the requirements file first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy specific project directories and files into the container
COPY microservices/ microservices/
COPY tests/ tests/
COPY docker/ docker/
COPY performance_tests/ performance_tests/
COPY .gitignore .
COPY README.md .

# Create a wrapper script for running tests
COPY docker/test/wait-and-test.sh /app/wait-and-test.sh
RUN chmod +x /app/wait-and-test.sh

# Expose any necessary ports (if needed for debugging)
EXPOSE 8080

# Command to run tests
CMD ["./wait-and-test.sh"]
