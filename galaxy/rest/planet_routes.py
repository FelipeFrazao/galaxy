import logging

from app import app
from galaxy.builders.planet_builder import build_planet_list, build_planet_by_id


@app.route("/v1/planets/", methods=['GET'])
@app.route("/planets/", methods=['GET'])
def get_planet_list():
    logging.debug("[GET] /planets/")
    resp = build_planet_list()
    return resp


@app.route("/planets/<planetid>/")
@app.route("/v1/planets/<planetid>/")
def get_planet_by_id(planetid):
    logging.debug("[GET] /planets/%s" % planetid)
    resp = build_planet_by_id(planetid)
    return resp
