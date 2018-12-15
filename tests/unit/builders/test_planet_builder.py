from flask_testing import TestCase

from app import app
from unittest.mock import patch
from galaxy.builders.planet_builder import build_planet_list, build_planet_by_id
from galaxy.domain.planet import Planet
from galaxy.repository.planet_repository import PlanetRepository
from galaxy.services.sw_api_service import SwApiService

list_expected = [
    {
        "_id": "80884966-d276-4066-9f6c-718ce2ffc11e",
        "name": "Yavin IV",
        "climate": ["temperate", "tropical"],
        "terrain": ["jungle", "rainforests"],
        "apparitions": 1,
        "population": 1000
    },
    {
        "_id": "80884966-d276-4066-9f6c-718ce2ffc11e",
        "name": "Yavin IV",
        "climate": ["temperate", "tropical"],
        "terrain": ["jungle", "rainforests"],
        "apparitions": 1,
        "population": 1000
    },
    {
        "_id": "80884966-d276-4066-9f6c-718ce2ffc11e",
        "name": "Yavin IV",
        "climate": ["temperate", "tropical"],
        "terrain": ["jungle", "rainforests"],
        "apparitions": 1,
        "population": 1000
    }
]
sw_api_mock = {
            "name": "Yavin IV",
            "rotation_period": "24",
            "orbital_period": "4818",
            "diameter": "10200",
            "climate": "temperate, tropical",
            "gravity": "1 standard",
            "terrain": "jungle, rainforests",
            "surface_water": "8",
            "population": "1000",
            "residents": [],
            "films": [
                "https://swapi.co/api/films/1/"
            ],
            "created": "2014-12-10T11:37:19.144000Z",
            "edited": "2014-12-20T20:58:18.421000Z",
            "url": "https://swapi.co/api/planets/3/"
        }
planet_list_repo_mock = [
    Planet(
            _id="80884966-d276-4066-9f6c-718ce2ffc11e",
            name="Yavin IV",
            climate=["temperate", "tropical"],
            terrain=["jungle", "rainforests"],
            apparitions=None,
            population=None,
        ),
    Planet(
            _id="80884966-d276-4066-9f6c-718ce2ffc11e",
            name="Yavin IV",
            climate=["temperate", "tropical"],
            terrain=["jungle", "rainforests"],
            apparitions=None,
            population=None,
        ),
    Planet(
            _id="80884966-d276-4066-9f6c-718ce2ffc11e",
            name="Yavin IV",
            climate=["temperate", "tropical"],
            terrain=["jungle", "rainforests"],
            apparitions=None,
            population=None,
        ),
]
planet_by_id_mock = Planet(_id="80884966-d276-4066-9f6c-718ce2ffc11e", name="Yavin IV", climate=["temperate", "tropical"], terrain=["jungle", "rainforests"], apparitions=None, population=None,)
planet_by_id_expec = {
        "_id": "80884966-d276-4066-9f6c-718ce2ffc11e",
        "name": "Yavin IV",
        "climate": ["temperate", "tropical"],
        "terrain": ["jungle", "rainforests"],
        "apparitions": 1,
        "population": 1000
    }


class TestUnitPlanetBuilder(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    @patch.object(PlanetRepository, "get_planet_list", return_value=planet_list_repo_mock)
    @patch.object(SwApiService, "get_planet_info", return_value=sw_api_mock)
    def test_build_planet_list(self, mock_planet_repository, mock_sw_api_service):
        planets_result = build_planet_list()
        assert planets_result, list_expected

    @patch.object(PlanetRepository, "get_planet_by_id", return_value=planet_by_id_mock)
    @patch.object(SwApiService, "get_planet_info", return_value=sw_api_mock)
    def test_build_planet_by_id(self, mock_planet_repository, mock_sw_api_service):
        planet_result = build_planet_by_id("80884966-d276-4066-9f6c-718ce2ffc11e")
        assert planet_by_id_expec, planet_result