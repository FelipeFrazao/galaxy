class Planet(object):
    def __init__(self, name: str, climate: str, terrain: str, apparitions=None, population=None):
        """
        :arg:

        :rtype: Planet
        """
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.apparitions = apparitions
        self.population = population

    def to_dict(self):
        return {
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "apparitions": self.apparitions,
            "population": self.population,
        }


