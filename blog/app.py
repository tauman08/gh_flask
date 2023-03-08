from flask import Flask

from blog import commands
from blog.extensions import db, login_manager
from blog.models import User
from blog.config import Development


def create_app() -> Flask:
    app = Flask(__name__)
    #app.config.from_object(Development)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog.auth.views import auth
    from blog.user.views import user
    from blog.report.views import report
    from blog.articles.views import article

    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(report)
    app.register_blueprint(article)

#


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)


# from flask import Flask, redirect, url_for
# from flask_login import LoginManager
# from blog.config import Development
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
# login_manager = LoginManager()
#
# from blog.auth.views import auth
# from blog.report.views import report
# from blog.user.views import user
# from blog.articles.views import article
#
#
#
# def create_app() -> Flask:
#     from .models import User
#     app = Flask(__name__)
#     app.config.from_object(Development)
#
#
#     db.init_app(app)
#
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)
#
#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))
#
#     # @login_manager.unauthorized_handler
#     # def unauthorized():
#     #     return redirect(url_for("auth.login"))
#
#     register_blueprints(app)
#     return app
#
#
# def register_blueprints(app: Flask):
#     app.register_blueprint(user)
#     app.register_blueprint(report)
#     app.register_blueprint(article)
#     app.register_blueprint(auth)
#
