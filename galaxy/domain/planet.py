import uuid


class Planet(object):
    def __init__(self, name: str, climate: str, terrain: str, apparitions=None, population=None):
        """

        :param name: (str) Planet's name
        :param climate: (str) Planet's climate
        :param terrain: (str) Planet's terrain
        :param apparitions: (str) Planet's apparitions in films
        :param population: (str) Planet's population
        """
        self._id = uuid.uuid4()
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.apparitions = apparitions
        self.population = population

    def to_dict(self) -> dict:
        """
        :return: dict
        """
        return {
            "id": self._id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "apparitions": self.apparitions,
            "population": self.population,
        }

    def add_outhers_infos(self, apparitions: str, population: str):
        """

        :param apparitions:
        :param population:
        :return: None
        """
        self.apparitions = apparitions
        self.population = population
