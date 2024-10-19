# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
#ex: ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
ADD . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



