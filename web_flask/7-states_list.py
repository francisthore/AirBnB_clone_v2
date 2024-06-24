#!/usr/bin/python3
"""Lists the states in the database"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Makes db query and returns dict of states"""
    states_l = storage.all(State)
    return render_template('7-states_list.html', states=states_l)


@app.teardown_appcontext
def teardown_db(exception):
    """closes storage instance"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
