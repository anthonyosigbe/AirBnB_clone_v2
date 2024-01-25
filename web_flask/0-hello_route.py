#!/usr/bin/python3
"""Initiate a Flask-based web application."""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_flask():
    """Provide a string as a response 'Hello HBNB!
    when the route is accessed."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
