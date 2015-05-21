#!/usr/local/bin/python

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def toppage():
    return render_template('top.html')

if __name__ == '__main__':
    app.run(debug = True)


