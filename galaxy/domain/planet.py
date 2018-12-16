import uuid


class Planet(object):
    def __init__(self, name: str, climate: list, terrain: list, apparitions=None, population=None, _id=None):
        """
        :param name: (str) Planet's name
        :param climate: (str) Planet's climate
        :param terrain: (str) Planet's terrain
        :param apparitions: (int) Planet's apparitions in films
        :param population: (int) Planet's population
        """
        if _id is None:
            self._id = uuid.uuid4()
        else:
            self._id = _id
        self.name = name
        self.climate = climate
        self.terrain = terrain
        if apparitions is None:
            self.apparitions = None
        else:
            self.apparitions = apparitions
        if population is None:
            self.population = None
        else:
            self.population = population

    def to_dict(self) -> dict:
        """
        :return: dict
        """
        return {
            "_id": self._id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "apparitions": self.apparitions,
            "population": self.population,
        }

    @classmethod
    def from_dict(cls, planet_dict):
        planet = Planet(
            _id=planet_dict["_id"],
            name=planet_dict["name"],
            climate=planet_dict["climate"],
            terrain=planet_dict["terrain"],
            apparitions=planet_dict["apparitions"] if "apparitions" in planet_dict else None,
            population=planet_dict["population"] if "population" in planet_dict else None,
        )
        return planet

    def add_outhers_infos(self, apparitions: str, population: str):
        """
        :param apparitions:
        :param population:
        :return: None
        """
        self.apparitions = apparitions
        self.population = population
