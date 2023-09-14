FROM python:3.11-slim

COPY ./src /app/src
COPY ./requirements.txt /app
COPY ./docker /app/docker

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000