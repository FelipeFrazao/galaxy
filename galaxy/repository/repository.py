import abc


class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_planet_list(self):
        pass

    @abc.abstractmethod
    def get_planet_by_id(self, id):
        pass

    @abc.abstractmethod
    def get_planet_by_name(self, name):
        pass

    @abc.abstractmethod
    def insert(self, planet):
        pass

    @abc.abstractmethod
    def delete_planet(self, id):
        pass
