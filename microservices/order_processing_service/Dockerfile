# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file from the project root into the container
COPY ../../requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port that the service will run on
EXPOSE 5004

# Command to run the service
CMD ["python", "order_processing_service.py"]