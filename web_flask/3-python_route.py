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
def c_text(text):
    """ A function that  echos back a variable passed to it at /c/text """
    return "C %s" % escape(text.replace("_", " "))


@app.route("/python/(<text>)", strict_slashes=False)
def python_text(text="so cool"):
    return "Python %s" % escape(text.replace("_", " "))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
