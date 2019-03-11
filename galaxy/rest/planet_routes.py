import logging
import json

from flask import request

from app import app
from galaxy.builders.planet_builder import build_planet_by_id, build_insert_planet
from galaxy.builders.planet_builder import build_planet_by_name
from galaxy.builders.planet_builder import build_planet_delete
from galaxy.builders.planet_builder import build_planet_list


@app.route("/v1/planet/", methods=["GET"])
@app.route("/planet", methods=["GET"])
@app.cache.cached(timeout=300)
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
@app.cache.cached(timeout=300)
def get_planet_by_id(planetid):
    logging.debug("[GET] /planet/%s" % planetid)
    resp = build_planet_by_id(planetid)
    return resp


@app.route("/planet/<planetid>/", methods=["DELETE"])
@app.route("/v1/planet/<planetid>/", methods=["DELETE"])
def delete_planet(planetid):
    logging.debug("[DELETE] /planet/%s" % planetid)
    resp = build_planet_delete(planetid)
    return resp


@app.route("/planet/", methods=["POST"])
@app.route("/v1/planet/", methods=["POST"])
def insert_planet():
    planet = request.json
    planet = json.dumps(planet)
    planet_dict = json.loads(planet)
    resp = build_insert_planet(planet_dict)
    return resp
