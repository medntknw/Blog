from flask import Blueprint, render_template, redirect, url_for, request,flash
from flask_login import login_required, current_user
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Blogs
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Blogs.query.order_by(Blogs.id.desc()).limit(3).all()
    return render_template('index.html', data=posts)

@login_required
@main.route('/', methods=['POST'])
def index_post():
    post = request.form.get('post')
    email = current_user.email
    new_post = Blogs(email_id=email,post=post)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('main.index'))



@login_required
@main.route('/profile')
def profile():
    name = current_user.name
    return render_template('profile.html', name=name)