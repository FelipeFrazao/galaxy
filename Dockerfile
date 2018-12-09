FROM python:3.6.2rc2
LABEL maintainer "felipe.sfrazao@outlook.com"
ENV PYTHONUNBUFFERED 1

EXPOSE 3000

RUN mkdir /galaxy
WORKDIR /galaxy

ADD . /galaxy

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements_dev.txt
