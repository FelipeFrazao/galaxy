import os

from pymongo import MongoClient


class MongoRepository(object):
    def __init__(self):
        mongo_connection_string = os.environ.get("MONGO_CONNECTION_STRING")
        self.client = MongoClient(mongo_connection_string)
        self.star_wars_db = self.client.starwars
        self.planets_collection = self.star_wars_db.planets
