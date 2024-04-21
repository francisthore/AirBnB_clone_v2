#!/usr/bin/python3
"""Starts a Flask Web Application
on Localhost"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
