#!/usr/bin/python3
"""A script that runs a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """HBNB route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun_route(text):
    """Takes in a parameter"""
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Takes a text variable but has default value"""
    return 'Python {}'.format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
