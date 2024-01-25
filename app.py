from flask import flask

app = flask(__name__)

@app.route('/')
def hellow_world():
    return 'hellow world'