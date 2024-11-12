# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the service will run on
EXPOSE 5005

# Command to run the service
CMD ["python", "notification_service.py"]