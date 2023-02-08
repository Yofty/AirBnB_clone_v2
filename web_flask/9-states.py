#!/usr/bin/python3
"""Starts a flask web app"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """disply html page"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=states)
    return render_template("9-states.html")


@appteardown_appcontext
def teardown(exc):
    """remove current SQLAlchemy"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
