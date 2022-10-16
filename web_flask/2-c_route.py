#!/usr/bin/python3
"""
 Flask App that display a string at /, /hbnb and /c/<variable>
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


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C %s" % escape(text)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
