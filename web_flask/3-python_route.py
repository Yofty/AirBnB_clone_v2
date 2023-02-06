#!/usr/bin/python3
"""Starts flask web app"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hbnb_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    text = text.replace("_", " ")
    return "python %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
