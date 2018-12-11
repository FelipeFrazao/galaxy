from flask_testing import TestCase
from app import app
from galaxy.domain.planet import Planet
from galaxy.repository.planet_repository import PlanetRepository


class TestPlaneyRespository(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.planet_repo = PlanetRepository()
        self.planet_expected = Planet(
            _id="80884966-d276-4066-9f6c-718ce2ffc11e",
            name="Yavin IV",
            climate=["temperate", "tropical"],
            terrain=["jungle", "rainforests"],
        )

    def test_get_planet_by_id(self):
        planet = self.planet_repo.get_planet_by_id("80884966-d276-4066-9f6c-718ce2ffc11e")
        self.assertEqual(planet._id, self.planet_expected._id)
        self.assertEqual(planet.name, self.planet_expected.name)
        self.assertEqual(planet.climate, self.planet_expected.climate)
        self.assertEqual(planet.terrain, self.planet_expected.terrain)
        self.assertEqual(planet.apparitions, self.planet_expected.apparitions)
        self.assertEqual(planet.population, self.planet_expected.population)

    def test_get_planet_by_name(self):
        self.assertEqual(self.planet_repo.get_planet_by_name("Yavin IV"), [self.planet_expected])
