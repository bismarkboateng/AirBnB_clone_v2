#!/usr/bin/python3
# running flask on all ips

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ A route that displays Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
