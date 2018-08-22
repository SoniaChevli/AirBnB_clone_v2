#!/usr/bin/python3
'''
starts flask
runs on 0.0.0.0, port 5000
'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    ''' /: display “Hello HBNB!” '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    ''' /hbnb: display “HBNB” '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' /c/<text>: displays C followed by the given text '''
    return ('C {}'.format(str(text)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
