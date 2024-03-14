FROM python:3.10.2-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY Main.py .

EXPOSE 8000

ENTRYPOINT ["python","Main.py"]