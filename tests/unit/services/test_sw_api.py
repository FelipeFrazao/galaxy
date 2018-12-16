from unittest.mock import patch

from app import app
from flask_testing import TestCase
from galaxy.services.sw_api_service import SwApiService

json_expected = {
    "name": "Tatooine",
    "rotation_period": "23",
    "orbital_period": "304",
    "diameter": "10465",
    "climate": "arid",
    "gravity": "1 standard",
    "terrain": "desert",
    "surface_water": "1",
    "population": "200000",
    "residents": [
        "https://swapi.co/api/people/1/",
        "https://swapi.co/api/people/2/",
        "https://swapi.co/api/people/4/",
        "https://swapi.co/api/people/6/",
        "https://swapi.co/api/people/7/",
        "https://swapi.co/api/people/8/",
        "https://swapi.co/api/people/9/",
        "https://swapi.co/api/people/11/",
        "https://swapi.co/api/people/43/",
        "https://swapi.co/api/people/62/",
    ],
    "films": [
        "https://swapi.co/api/films/5/",
        "https://swapi.co/api/films/4/",
        "https://swapi.co/api/films/6/",
        "https://swapi.co/api/films/3/",
        "https://swapi.co/api/films/1/",
    ],
    "created": "2014-12-09T13:50:49.641000Z",
    "edited": "2014-12-21T20:48:04.175778Z",
    "url": "https://swapi.co/api/planets/1/",
}
mocK_execute_request = {
    "count": 1,
    "next": None,
    "previous": None,
    "results": [
        {
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000",
            "residents": [
                "https://swapi.co/api/people/1/",
                "https://swapi.co/api/people/2/",
                "https://swapi.co/api/people/4/",
                "https://swapi.co/api/people/6/",
                "https://swapi.co/api/people/7/",
                "https://swapi.co/api/people/8/",
                "https://swapi.co/api/people/9/",
                "https://swapi.co/api/people/11/",
                "https://swapi.co/api/people/43/",
                "https://swapi.co/api/people/62/",
            ],
            "films": [
                "https://swapi.co/api/films/5/",
                "https://swapi.co/api/films/4/",
                "https://swapi.co/api/films/6/",
                "https://swapi.co/api/films/3/",
                "https://swapi.co/api/films/1/",
            ],
            "created": "2014-12-09T13:50:49.641000Z",
            "edited": "2014-12-21T20:48:04.175778Z",
            "url": "https://swapi.co/api/planets/1/",
        }
    ],
}


class TestUnitSwApiService(TestCase):
    """
        Unit test for Service SwApi
    """

    def create_app(self):
        app.config["TESTING"] = True
        return app

    @patch.object(SwApiService, "execute_request", return_value=mocK_execute_request)
    def test_get_planet_info(self, mock_infos_planet):
        planet_result = SwApiService().get_planet_info("Tatooine")

        self.assertEqual(planet_result, json_expected)
