#!/usr/bin/python3
"""Initiate a Flask-based web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Shows 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_flask():
    """Provide a string as a response 'Hello HBNB!
    when the route is accessed."""
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Shows 'HBNB'."""
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
