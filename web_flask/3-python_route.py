#!/usr/bin/python3
"""Launch the web application with two routes.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Provide a string in response to a queried route.
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """When the route is queried, return a string.
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat the text based on the presence
    of an optional variable."""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
