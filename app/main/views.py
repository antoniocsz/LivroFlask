from flask import render_template, abort
from . import main
from ..models import User

# Views
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)
