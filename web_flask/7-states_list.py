#!/usr/bin/python3
'''
listens on 0.0.0.0 port 5000
'''
from models import storage
from flask import Flask, render_template
import operator

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    ''' /states_list: adds a list of states to html '''
    states = storage.all("State")
    state_list = list(states.values())

    return render_template('7-states_list.html', states=state_list)


@app.teardown_appcontext
def teardown(value):
    ''' remove the current SQLAlchemy Session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
