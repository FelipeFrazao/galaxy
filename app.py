"""
    Start project
    isort: skip_file
"""
# flake8: noqa F401 F402
from flask import Flask
import logging
from flask_caching import Cache

app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)

app.config["CACHE_TYPE"] = "simple"

# instancie o cache e atribua a sua aplicação
app.cache = Cache(app)

if __name__ == "__main__":
    app.run()


# Inicialize routes
from galaxy.rest import planet_routes
