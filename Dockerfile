# Use a specific version of Alpine-based Python image
FROM python:3.13.1-alpine3.21

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (required for some Python packages like zmq)
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Copy the requirements.txt file first to leverage Docker caching
COPY ./requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code from ../src
COPY ./src .

# Expose the port your application uses
EXPOSE 5555

# Run the application
CMD ["python", "main.py"]