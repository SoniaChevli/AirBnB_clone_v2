#!/usr/bin/python3
'''
starts a flask web application
'''
from models import storage
from flask import Flask, render_template
import os
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown(value):
    '''removes cirrent sqlalchemy session '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    ''' /states_list: adds a list of states to html '''
    if os.env('HBNB_TYPE_STORAGE') is 'db':
        states = storage.all(State)
    else:
        states = storage.all("State")
    state_list = list(states.values())

    return render_template('7-states_list.html', states=state_list)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' shows all the states with cities'''
    if os.env('HBNB_TYPE_STORAGE') is 'db':
        states = storage.all(State)
    else:
        states = storage.all("State")

    states = list(states.values())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    ''' listens on 0.0.0.0 port 5000'''
    app.run(host='0.0.0.0', port=5000)
