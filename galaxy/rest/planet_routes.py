import logging

from flask import request

from app import app
from galaxy.builders.planet_builder import build_planet_by_id
from galaxy.builders.planet_builder import build_planet_by_name
from galaxy.builders.planet_builder import build_planet_delete
from galaxy.builders.planet_builder import build_planet_list


@app.route("/v1/planet/", methods=["GET"])
@app.route("/planets", methods=["GET"])
def get_planet_list():
    name = request.args.get("name")
    if name is not None:
        logging.debug("[GET] /planet/?name=%s" % name)
        resp = build_planet_by_name(name)
        return resp
    logging.debug("[GET] /planet/")
    resp = build_planet_list()
    return resp


@app.route("/planet/<planetid>/")
@app.route("/v1/planet/<planetid>/")
def get_planet_by_id(planetid):
    logging.debug("[GET] /planet/%s" % planetid)
    resp = build_planet_by_id(planetid)
    return resp


@app.route("/planet/<planetid>/delete", methods=["DELETE"])
@app.route("/v1/planet/<planetid>/delete", methods=["DELETE"])
def delete_planet(planetid):
    logging.debug("[DELETE] /planet/%s" % planetid)
    resp = build_planet_delete(planetid)
    return resp
