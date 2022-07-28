from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask('henlo')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    content = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')
    
db.create_all()

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('blog.html', posts=posts)

@app.route('/populate')
def populate():
    user = User(username='Nunius', email='abc@def.com', password_hash='sdkdfdg')
    post1 = Post(title='first',content='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt ad porro voluptatibus at placeat facilis in odit corporis repudiandae atque iure fugit officia, eos voluptates officiis, sapiente temporibus libero debitis.', author=user)
    post2 = Post(title='second', content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo ipsam quam sapiente quidem iusto laudantium praesentium omnis quas nesciunt. Odit nesciunt quos expedita quam? Tenetur, est. Vitae minima nam accusamus.', author=user)
    post3 = Post(title='third', content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit recusandae, libero facere molestias ab quibusdam quas perspiciatis illo aperiam corrupti esse nostrum? Aperiam nesciunt rem ea magnam. Dolores, laborum totam.', author=user)
    db.session.add(user)
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()
    return redirect(url_for('index'))
