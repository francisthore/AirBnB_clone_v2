#!/usr/bin/python3
"""Lists the states in the database"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(e):
    """closes storage instance"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """Makes db query and returns dict of states"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
