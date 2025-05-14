FROM python:3.9-slim

RUN adduser --disabled-password appuser
USER appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

CMD ["python", "app.py"]
