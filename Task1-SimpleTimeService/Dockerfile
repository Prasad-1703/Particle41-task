FROM python:3.9-slim # For minimizing the size

ENV PYTHONUNBUFFERED=1  # To flush the output directly, not necessary to use it if logs are not necessary

RUN useradd -m appuser # To run the application by non-root user 

WORKDIR /app

COPY . . # This copies the application code i.e. app.py 

RUN pip install flask

USER appuser

EXPOSE 8080 # Expose port to access the application

CMD ["python", "app.py"]
