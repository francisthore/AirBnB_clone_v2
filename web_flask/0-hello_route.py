#!/usr/bin/python3
"""A script that runs a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Root route"""
    return 'Hello HBNB!'


@app.route('/airbnb-onepage', strict_slashes=False)
def airbnb():
    """Another route"""
    return 'Hellow HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
