from flask_login import UserMixin
from . import db

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Blogs', backref='name', lazy=True)

class Blogs(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(4096))
    email_id = db.Column(db.String(100),db.ForeignKey(User.email))
    