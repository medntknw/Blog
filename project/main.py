from flask import Blueprint,render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@login_required
@main.route('/profile')
def profile():
    name = current_user.name
    return render_template('profile.html', name=name)