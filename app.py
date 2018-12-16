from flask import Flask
import logging

app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


# Inicialize routes
from galaxy.rest import planet_routes
