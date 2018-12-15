import logging

from app import app
from galaxy.builders.planet_builder import build_planet_list


@app.route("/v1/planets/")
@app.route("/planets/")
def get_planet_list():
    logging.debug("[GET] /planets/")
    resp = build_planet_list()
    return resp
