from app import app
from galaxy.builders.planet_builder import build_planet_list


@app.route("/v1/planets/")
@app.route("/planets/")
def get_planet_list():
    resp = build_planet_list()
    return resp


@app.route('/test')
def test():
    return 'ddd World!'