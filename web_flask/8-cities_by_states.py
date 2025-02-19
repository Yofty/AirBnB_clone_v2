#!/usr/bin/python3
"""start a flask web app"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """displays an HTML"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """remove the SQLAlchemy"""
    storage.close()


if __name__ == ("__main__"):
    app.run(host="0.0.0.0")
