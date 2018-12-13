import os

import requests
from flask import abort
import logging


class SwApiService(object):
    def __init__(self):
        self.swapi_host = os.environ.get("SWAPI_HOST")

    def get_planet_info(self, name: str):
        path = "planets/?search=%s" % name
        planet = self.execute_request(path)
        apparitions = len(planet["films"])
        population = int(planet["population"])
        return apparitions, population

    def execute_request(self, path: str, throws_404=False):
        url = "%s%s" % (self.swapi_host, path)
        logging.info("[SWAPI_SERVICE] - Execute: %s" % url)
        headers = {"Content-Type": "application/json"}
        response = requests.get(url=url, headers=headers)
        json_val = response.json()
        if response.status_code == 500:
            logging.warning("[SWAPI_SERVICE] - ERROR 500 in %s" % url)
            abort(500)
        return json_val["results"][0]
