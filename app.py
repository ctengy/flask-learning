from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hellow_world():
    return render_template('index.html')

@app.route('/hi/')
def hellow_world():
    name = {'name':'RY'}
    return render_template('jinja.html',**name)