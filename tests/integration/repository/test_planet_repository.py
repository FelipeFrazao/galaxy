from flask_testing import TestCase
from app import app
from unittest.mock import patch
from galaxy.domain.planet import Planet
from galaxy.repository.planet_repository import PlanetRepository

planet1 = Planet("Test Planet", ["tropical", "ice"], ["jungle"], _id="1234ABC")
planet2 = Planet("Test Planet 1", ["tropical", "arid"], ["ocean"])
planet3 = Planet("Test Planet 2", ["arid"], ["temperate"])
planet4 = Planet("Test Planet 3", ["hell"], ["rainforests"])
test = 1
list_planet_expected = [planet1, planet2, planet3, planet4]


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
            apparitions=None,
            population=None,
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
        planets = self.planet_repo.get_planet_by_name("Yavin IV")
        planets_exp = [Planet(
            _id="80884966-d276-4066-9f6c-718ce2ffc11e",
            name="Yavin IV",
            climate=["temperate", "tropical"],
            terrain=["jungle", "rainforests"],
            apparitions=None,
            population=None,
        )]
        difference = list(set(planets) - set(planets_exp))
        self.assertEqual(len(difference), 0)

    @patch.object(PlanetRepository, "get_planet_list", return_value=list_planet_expected)
    def test_get_planet_list(self, mock_planets):
        planets = self.planet_repo.get_planet_list()

        difference = list(set(planets) - set(list_planet_expected))
        mock_planets.assert_called_once_with()
        self.assertEqual(len(difference), 0)

    @patch.object(PlanetRepository, "delete_planet", return_value=test)
    def test_delete_planet(self, mock_deleted):
        deleted_count = self.planet_repo.delete_planet("1234ABC")

        self.assertEqual(1, deleted_count)

    @patch.object(PlanetRepository, "insert", return_value="1234ABC")
    def test_insert(self, mock_insert):
        inserted_id = self.planet_repo.insert(planet1.to_dict())
        
        self.assertEqual(inserted_id, planet1.to_dict()["_id"])
