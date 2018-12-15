from flask import jsonify

from galaxy.domain.planet import Planet
from galaxy.repository.planet_repository import PlanetRepository
from galaxy.services.sw_api_service import SwApiService


def build_planet_list():
    planet_list = PlanetRepository().get_planet_list()
    for planet in planet_list:
        films, population = get_all_data_to_build_planet(planet)
        if films is not None:
            planet.add_outhers_infos(apparitions=len(films), population=population)

    return jsonify([planet.to_dict() for planet in planet_list])


def get_all_data_to_build_planet(planet: Planet):
    print(planet)
    if planet.apparitions is None or planet.population is None:
        planet_result = SwApiService().get_planet_info(planet.name)
        return planet_result["films"], int(planet_result["population"])
