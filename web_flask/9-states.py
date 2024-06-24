#!/usr/bin/python3
"""Lists the states in the database"""

from markupsafe import escape
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(e):
    """closes storage instance"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Lists cities grouped by states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<string:id>', strict_slashes=False)
def state(id):
    """Returns single state by id"""
    id = escape(id)
    state = [state for state in storage.all(State).values()
             if state.id == id]
    if state:
        state = state[0]
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
