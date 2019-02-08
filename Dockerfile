FROM python:3.7
LABEL maintainer "felipe.sfrazao@outlook.com"
ENV PYTHONUNBUFFERED 1

EXPOSE 3000 5005

RUN mkdir /galaxy
WORKDIR /galaxy

ADD . /galaxy

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements_dev.txt

# Copy Entrypoint script in the container
COPY ./docker-entrypoint.sh /
COPY .env /
RUN export $ cat env | xargs
ENTRYPOINT ["/docker-entrypoint.sh"]