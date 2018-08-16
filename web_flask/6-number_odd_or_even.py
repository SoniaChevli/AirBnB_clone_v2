#!/usr/bin/python3
'''
starts flask
runs on 0.0.0.0, port 5000
'''

from flask import Flask, render_template
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
    mystr = 'C {}'.format(text)
    return mystr.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    ''' /python displays python followed by text '''
    mystr = 'Python {}'.format(text)
    return mystr.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' checks if integer passed in is a number '''
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''add to html code by setting num param to int n'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_odd_even(n):
    tmpstr = 'odd'
    if n % 2 == 0:
        tmpstr = 'even'
    return render_template('6-number_odd_or_even.html', num=n,
                           evenORodd=tmpstr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
