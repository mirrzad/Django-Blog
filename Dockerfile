FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


COPY ./core /app/
