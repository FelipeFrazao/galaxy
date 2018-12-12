# from repository import
from galaxy.domain.planet import Planet
from galaxy.repository.mongo_repository import MongoRepository
from galaxy.repository.repository import Repository


class PlanetRepository(Repository):

    def __init__(self):
        super().__init__()
        self.mongo_client = MongoRepository()

    def get_planet_by_id(self, id):
        adict = self.mongo_client.planets_collection.find_one({"_id": id})
        planet = Planet.from_dict(adict)
        return planet

    def get_planet_list(self):
        planets = self.mongo_client.planets_collection.find()
        return [Planet.from_dict(planet) for planet in planets]

    def get_planet_by_name(self, name):
        planets = self.mongo_client.planets_collection.find({"name": name})
        print(list(planets))
        return [Planet.from_dict(planet) for planet in planets]

    def delete_planet(self, id):
        pass
