#!/usr/bin/python3
"""Flask problem to retrive dyanamic states
list"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders list of states to"""
    states = "statest"
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown():
    """Removes current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
