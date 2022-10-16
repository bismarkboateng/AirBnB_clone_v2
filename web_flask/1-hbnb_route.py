#!/usr/bin/python3
"""
 Flask App that display a string at / and /hbnb
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ A function  that displays Hello HBNB! on the root route / """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ A function that dispaly HBNB at /hbnb """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
