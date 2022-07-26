from flask import Flask, render_template

app = Flask('henlo')

@app.route('/')
def start():
    return 'henlo'

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/hai')
def hai():
    return render_template('index.html')

