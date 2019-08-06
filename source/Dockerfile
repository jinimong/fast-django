FROM python:3.6

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_READ_DOT_ENV_FILE 1

RUN pip install --upgrade pip
COPY . /usr/src/app/
RUN pip install -r requirements.txt

