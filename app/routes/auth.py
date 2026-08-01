from flask import Blueprint, render_template, request, redirect, url_for, flash

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import (
    login_user,
    logout_user,
    login_required
)

from app import db
from app.models.user import User


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        # Basic validation
        if not username or not email or not password:
            flash("All fields are required.", "warning")
            return redirect(url_for("auth.register"))

        # Prevent duplicate usernames
        existing_username = User.query.filter_by(
            username=username
        ).first()

        if existing_username:
            flash("That username is already taken.", "warning")
            return redirect(url_for("auth.register"))

        # Prevent duplicate email addresses
        existing_email = User.query.filter_by(
            email=email
        ).first()

        if existing_email:
            flash("An account with that email already exists.", "warning")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Account created successfully. You can now log in.",
            "success"
        )

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            flash(
                f"Welcome back, {user.username}!",
                "success"
            )

            return redirect(url_for("main.dashboard"))

        flash(
            "Invalid email or password.",
            "danger"
        )

        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "You have been logged out successfully.",
        "info"
    )

    return redirect(url_for("auth.login"))