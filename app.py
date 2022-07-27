from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask('henlo')

database = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('blog.html', posts=posts)
