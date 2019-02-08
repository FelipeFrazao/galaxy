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
ENV FLASK_APP app.py
ENV PORT 5005

# Star wars api
ENV SWAPI_HOST https://swapi.co/api/

# MongoDB
ENV MONGO_CONNECTION_STRING mongodb+srv://felipefrazao:felipefrazao21.@cluster0-tzcsp.mongodb.net/starwars
ENV STAR_WARS_DB star_wars_db
ENV PLANETS_COLLECTION planets

ENV GUNICORN_WORKS 1
ENV GUNICORN_MAX_REQUESTS 5000
ENV GUNICORN_DEBUG_TIMEOUT 3600
ENTRYPOINT ["/docker-entrypoint.sh"]