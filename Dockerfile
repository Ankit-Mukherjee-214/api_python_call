FROM python:3.12.7
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY routing.py .
EXPOSE  5000
CMD ["python", "routing.py"]