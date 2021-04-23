FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Expose port 80:
EXPOSE 80

# Copy the current local directory to the image's woking directory:
COPY ./app /app

RUN ["pip", "install", "-r", "requirements.txt"]

# Install dependecies:

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]