from flask import jsonify

from galaxy.domain.planet import Planet
from galaxy.repository.planet_repository import PlanetRepository
from galaxy.services.sw_api_service import SwApiService
import logging


def build_planet_list():
    logging.debug("[BULDER_PLANET_LIST]: Getting data to build the planet list")
    planet_list = PlanetRepository().get_planet_list()
    logging.info("[BULDER_PLANET_LIST]: Got planet list")
    logging.info("[BULDER_PLANET_LIST]: Build planets")
    for planet in planet_list:
        films, population = get_all_data_to_build_planet(planet)

        if films is not None:
            planet.add_outhers_infos(apparitions=len(films), population=population)

    logging.info("[BULDER_PLANET_LIST]: returning planet list json")
    return jsonify([planet.to_dict() for planet in planet_list])


def build_planet_by_id(id: str):
    logging.debug("[BULDER_PLANET_BY_ID]: Getting data to build the planet")
    planet = PlanetRepository().get_planet_by_id(id)
    logging.info("[BULDER_PLANET_BY_ID]: Got planet %s" % id)
    logging.info("[BULDER_PLANET_BY_ID]: Build planet")
    films, population = get_all_data_to_build_planet(planet)
    planet.add_outhers_infos(apparitions=len(films), population=population)
    planet = planet.to_dict()
    logging.info("[BULDER_PLANET_BY_ID]: returning planet %s json", id)
    return jsonify(planet)


def get_all_data_to_build_planet(planet: Planet):
    if planet.apparitions is None or planet.population is None:
        planet_result = SwApiService().get_planet_info(planet.name)
        films = planet_result["films"]

        try:
            population = int(planet_result["population"])
        except Exception as e:
            population = None

        return films, population
