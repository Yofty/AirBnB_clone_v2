#!/usr/bin/python3
"""starts flasx web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """remove the current SQLAlchemy"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
