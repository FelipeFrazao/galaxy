import os

from flask_testing import TestCase
from unittest import mock

from app import app
from galaxy.services.sw_api_service import SwApiService


class TestUnitSwApiService(TestCase):
    """
        Unit test for Service SwApi
    """

    def create_app(self):
        app.config['TESTING'] = True
        return app

    @mock.patch.dict(os.environ, {"SWAPI_HOST": "https://swapi.co/api/"})
    def test_get_planet_info(self):
        apparitions, population = SwApiService().get_planet_info("Tatooine")
        self.assertEqual(apparitions, 5)
        self.assertEqual(population, 200000)

    # def test_execute_request(self):
    #     SwApiService.execute_request("planets/?=Tatooine")
