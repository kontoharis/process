# Use an official Python runtime as a parent image

FROM python:3.8-slim

 

# Set the working directory in the container

WORKDIR /app

 

# Install libgl1-mesa-glx to provide libGL.so.1

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

 

# Copy the requirements file into the container at /app

COPY requirements.txt /app/

 

# Install any needed packages specified in requirements.txt

RUN pip install -r requirements.txt

 

# Copy the current directory contents into the container at /app

COPY . /app/

 

# Make port 80 available to the world outside this container

EXPOSE 80

 

# Define environment variable for Flask

ENV FLASK_APP app.py

 

# Run app.py when the container launches

CMD ["flask", "run", "--host=13.51.204.248", "--port=80"]