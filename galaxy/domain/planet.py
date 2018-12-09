class Planet(object):
    def __init__(self, name: str, climate: str, terrain: str, apparitions=None, population=None):
        """

        :param name: (str) Planet's name
        :param climate: (str) Planet's climate
        :param terrain: (str) Planet's terrain
        :param apparitions: (str) Planet's apparitions in films
        :param population: (str) Planet's population
        """

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
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "apparitions": self.apparitions,
            "population": self.population,
        }

    def add_outhers_info(self, apparitions: str = None, population: str = None):
        """

        :param apparitions:
        :param population:
        :return: None
        """
        self.apparitions = apparitions
        self.population = population
