# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

ENTRYPOINT ["python"]

CMD ["app.py"]