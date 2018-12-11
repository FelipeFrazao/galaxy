from flask_testing import TestCase
import uuid

from app import app
from galaxy.domain.planet import Planet


class TestPlanetModel(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        self.planet = Planet("Test Planet", ["tropical"], ["jungle"])
        self.uid = str(uuid.uuid4())
        self.planet._id = self.uid
        return app

    def test_planet_model_init(self):
        self.assertEqual(self.planet.name, "Test Planet")
        self.assertEqual(self.planet.climate, ["tropical"])
        self.assertEqual(self.planet.terrain, ["jungle"])

    def test_planet_model_to_dict(self):
        dict_planet = {
            "_id": self.uid,
            "name": "Test Planet",
            "climate": ["tropical"],
            "terrain": ["jungle"],
            "apparitions": None,
            "population": None,
        }
        planet_dict = self.planet.to_dict()
        self.assertEqual(planet_dict, dict_planet)

    def test_planet_model_add_outhers_infos(self):
        self.planet.add_outhers_infos(6, 1000)
        self.assertEqual(6, self.planet.apparitions)
        self.assertEqual(1000, self.planet.population)
