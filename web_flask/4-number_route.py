#!/usr/bin/python3
"""starts flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """printe hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints c followed by text argument"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints python followed text argument/is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """prints n is a number if n is integer"""
    return "%i is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0")
