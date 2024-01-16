# All routes related to authentication
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in! ")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("password is incorrect. ", category="error")
        else:
            flash("email does not exist. ", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(
            email=email
        ).first()  # looks in User database. Filters the database by email
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash("Email is already in use. ", category="error")
        elif username_exists:
            flash("Username is already in use. ", category="error")
        elif password1 != password2:
            flash("Passwords do not match ", category="error")
        elif len(username) < 2:
            flash("Username must be longer than 2 characters. ", category="error")
        elif len(password1) < 6:
            flash("Password must be greater than 6 characters. ", category="error")
        elif len(email) < 4:
            flash("Email is invalid. ", category="error")
        else:
            new_user = User(
                email=email,
                username=username,
                password=generate_password_hash(password1, method="pbkdf2:sha256"),
            )
            db.session.add(new_user)  # add the variable that stores your user object
            db.session.commit()  # adds to database
            login_user(new_user, remember=True)
            flash("User Created! ")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)


@auth.route("/logout")
# login_required decorater, makes it so you can only access this page if you have been logged in.
# Only if login_user function has been called for your current user session are you able to access this root
@login_required
def log_out():
    logout_user()
    return redirect(url_for("views.home"))  # refrencing the home() function
