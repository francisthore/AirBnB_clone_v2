#!/usr/bin/python3
"""A script that runs a Flask web application"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays n only is its int"""
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Renders a template and displays a number"""
    return render_template('5-number.html', n=escape(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
