import os

from flask_testing import TestCase

from app import app
from galaxy.services.SwApiService import SwApiService


class TestIntegrationSWApi(TestCase):
    def __init__(self):
        self.swapi_host = os.environ.get("SWAPI_HOST")

    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_get_planets_info(self):
        apparitions, population = SwApiService().get_planets_info("Tatooine")
        self.assertEqual(apparitions, 5)
        self.assertEqual(population, 200000)
