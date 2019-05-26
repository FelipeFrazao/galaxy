"""
    Start project
    isort: skip_file
"""
# flake8: noqa F401 F402
from flask import Flask
import logging

from galaxy.rest.planet_routes import planet_blueprint
from galaxy.services.cache_service import cache

app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)

app.config["CACHE_TYPE"] = "simple"
cache.init_app(app)

if __name__ == "__main__":
    app.run()

# Inicialize routes
app.register_blueprint(planet_blueprint)
