from flask import Flask  # import flask
from flask_sqlalchemy import SQLAlchemy  # import SQLALchemy
from os import path
from flask_login import LoginManager

# create database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():  # create flask application and return it
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hello world"  # encrypt session data
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"  # configure database
    db.init_app(app)

    # relative import because we are inside a python package
    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created database!")
