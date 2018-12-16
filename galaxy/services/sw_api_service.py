import logging
import os

import requests

from app import app


class SwApiService(object):
    def __init__(self):
        self.swapi_host = os.environ.get("SWAPI_HOST")

    def get_planet_info(self, name: str):
        path = "planets/?search=%s" % name
        planet = self.execute_request(path)
        return planet["results"][0]

    @app.cache.cached(timeout=300)
    def execute_request(self, path: str):
        url = "%s%s" % (self.swapi_host, path)
        logging.info("[SWAPI_SERVICE] - Execute: %s" % url)
        headers = {"Content-Type": "application/json"}
        response = requests.get(url=url, headers=headers)
        json_val = response.json()
        if response.status_code == 500:
            logging.warning("[SWAPI_SERVICE] - ERROR 500 in %s" % url)
        return json_val
