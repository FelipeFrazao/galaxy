import logging

from galaxy.domain.planet import Planet
from galaxy.repository.mongo_repository import MongoRepository
from galaxy.repository.repository import Repository


class PlanetRepository(Repository):
    def __init__(self):
        super().__init__()
        self.mongo_client = MongoRepository()

    def insert(self, planet: dict) -> str:
        write_result = self.mongo_client.planets_collection.insert_one(planet)
        return write_result.inserted_id

    def get_planet_by_id(self, id: str) -> Planet:
        adict = self.mongo_client.planets_collection.find_one({"_id": id})
        if adict is not None:
            planet = Planet.from_dict(adict)
            return planet

    def get_planet_list(self) -> list:
        planets = self.mongo_client.planets_collection.find()
        return [Planet.from_dict(planet) for planet in planets]

    def get_planet_by_name(self, name: str) -> list:

        query = {"name": {"$regex": name, "$options": "i"}}
        print(query)
        logging.info("[GET PLANETS BY NAME]: query %s" % query)
        planets = self.mongo_client.planets_collection.find(query)
        planets = list(planets)
        return [Planet.from_dict(planet) for planet in planets]

    def delete_planet(self, id: str) -> int:
        delete_result = self.mongo_client.planets_collection.delete_one({"_id": id})
        return delete_result.deleted_count
