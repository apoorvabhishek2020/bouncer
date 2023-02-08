FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

RUN apt-get update -y && \
    apt-get upgrade -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
