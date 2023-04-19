# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY inclusive-thesaurus.py .

COPY inclusive-training-data.csv .

ENV INPUT_TEXT="Your default input text goes here."

CMD ["python", "inclusive-thesaurus.py"]
