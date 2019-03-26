# Image
FROM python:3.7-alpine

# Installing necessary components
RUN apk add musl-dev gcc tzdata bash
LABEL maintainer "felipe.sfrazao@outlook.com"
ENV PYTHONUNBUFFERED 1

EXPOSE 3000

RUN mkdir /galaxy
WORKDIR /galaxy

ADD . /galaxy

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements_dev.txt
