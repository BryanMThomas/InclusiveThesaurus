# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY converter.py ./

COPY output.json ./

CMD ["python", "converter.py"]
