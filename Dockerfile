# Use python:3.9-slim-buster as the base image
FROM python:3.9-slim-buster

WORKDIR /app
# Copy the application code and the requirements.txt file to the image
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

# Define the command that runs the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
