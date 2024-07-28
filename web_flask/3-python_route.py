#!/usr/bin/python3
"""Script that start a web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """C is fun"""
    formated_text = text.replace('_', ' ')
    return f"C {formated_text}"


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Python page"""
    formated_text = text.replace('_', ' ')
    return f"Python {formated_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
