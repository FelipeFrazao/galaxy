from app import app


@app.route("/v1/planets/")
@app.route("/planets/")
def get_planet_list():
    pass
