from unittest.mock import patch

from flask_testing import TestCase
from flask import jsonify

from app import app
from galaxy.rest.planet_routes import *


class TestUnitPlanetRoutes(TestCase):
    """"
    Unit test all methods on Planet routes
    """

    def create_app(self):
        app.config['TESTING'] = True
        return app

    @patch("galaxy.rest.planet_routes.get_planet_list")
    def test_get_planet_list_route(self, mock_builder):
        mock_builder.return_value = jsonify({})

