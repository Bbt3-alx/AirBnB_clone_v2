#!/usr/bin/python3
# Start a web application


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Home page"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ C is fun """
    formated_text = text.replace('_', ' ')
    return f"C {formated_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Python page"""
    formated_text = text.replace('_', ' ')
    return f"Python {formated_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """numbe page"""
    return f"{int(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Number template page"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
