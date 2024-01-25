#!/usr/bin/python3
"""Initiate a web application with two routes."""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
   """Respond with a string when the route is accessed."""
   return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Provide the reformatted text."""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
