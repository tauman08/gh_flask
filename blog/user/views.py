from flask import Blueprint, render_template, redirect
from flask_login import login_required
# from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

from blog.models import User


@user.route('/')
def user_list():

    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )

@user.route('/<int:pk>')
@login_required
def profile(pk: int):

    try:
        user_row = User.query.filter_by(id=pk).one_or_none()
        if user_row != None:
            user_name =  user_row.email
        else:
            user_name = 'None'

    except KeyError:
        # raise NotFound(f'User id {pk} not found')
        return redirect(
            '/users/'
        )

    return  render_template(
        'users/profile.html',
        user_name = user_name,
    )