import os

from flask_testing import TestCase

from unittest.mock import MagicMock
from unittest.mock import patch

from app import app
from galaxy.services.sw_api_service import SwApiService


class TestUnitSwApiService(TestCase):
    """
        Unit test for Service SwApi
    """

    def create_app(self):
        app.config['TESTING'] = True
        return app

    # @patch.dict(os.environ, {"SWAPI_HOST": "https://swapi.co/api/"})
    # @patch("galaxy.services.sw_api_service.SwApiService.get_planet_info", new=MagicMock())
    @patch.object(SwApiService, "get_planet_info", return_value=(5, 200000))
    def test_get_planet_info(self, mock_infos_planet):
        apparitions, population = SwApiService().get_planet_info("Tatooine")

        self.assertEqual(apparitions, 5)
        self.assertEqual(population, 200000)

    # def test_execute_request(self):
    #     SwApiService.execute_request("planets/?=Tatooine")
