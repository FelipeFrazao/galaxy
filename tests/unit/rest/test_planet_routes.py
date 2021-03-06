from unittest.mock import patch

from flask import jsonify

from app import app
from flask_testing import TestCase
from galaxy.rest.planet_routes import get_planet_list


class TestUnitPlanetRoutes(TestCase):
    """"
    Unit test all methods on Planet routes
    """

    def create_app(self):
        app.config["TESTING"] = True
        return app

    def setUp(self):
        self.list_planet = [
            {
                "_id": "80884966-d276-4066-9f6c-718ce2ffc11e",
                "name": "Yavin IV",
                "climate": ["temperate", "tropical"],
                "terrain": ["jungle", "rainforests"],
                "apparitions": 4,
                "population": 20000,
            },
            {
                "_id": "5dda99a9-335a-4768-8ed7-0acb9f59944a",
                "name": "Tatooine",
                "climate": ["arid"],
                "terrain": ["desert"],
                "apparitions": 2,
                "population": 23000,
            },
            {
                "_id": "cf0aba97-da17-4e8c-bc58-8b5418cb7efa",
                "name": "Alderaan",
                "climate": ["temperate"],
                "terrain": ["grasslands", "mountains"],
                "apparitions": 3,
                "population": 200,
            },
        ]

    def test_if_app_up_on_create_app(self):
        """
            Unit: Route: : Test if create_app is working.
        """
        self.assertIsNot(app, None)
        self.assertEqual(self.app.config["TESTING"], True)

    @patch("galaxy.rest.planet_routes.build_planet_list")
    def test_get_planet_list_route(self, mock_builder):
        """
            Unit: Route: Planet: Test method in route /planets/
        """
        mock_builder.return_value = self.list_planet

        planets_expec = get_planet_list()
        assert planets_expec, self.list_planet
