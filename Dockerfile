# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install OpenCV dependencies
RUN apt-get update && \
    apt-get install -y libsm6 libxext6 libxrender-dev && \
    rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip install --no-cache-dir opencv-python-headless

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files to the container
COPY main.py /app/
COPY image.jpg /app/

# Set the default command to run the script with the image
CMD ["python", "main.py", "/app/image.jpg"]
