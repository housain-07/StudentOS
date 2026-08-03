from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app import db
from app.models.task import Task
from app.models.user import User

main = Blueprint("main", __name__)


# =========================================================
# Helper Functions
# =========================================================

def get_user_task(task_id):
    """
    Retrieve a task and verify that it belongs
    to the currently logged-in user.

    Raises:
        404: If the task does not exist.
        403: If the task belongs to another user.
    """

    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        abort(403)

    return task


# =========================================================
# Public Routes
# =========================================================

@main.route("/")
def home():
    return render_template("index.html")


# =========================================================
# Dashboard
# =========================================================

@main.route("/dashboard")
@login_required
def dashboard():

    subjects = 8
    study_hours = 0
    cgpa = 3.87

    # Only retrieve tasks belonging to the logged-in user
    study_tasks = current_user.tasks
    tasks = len(study_tasks)

    return render_template(
        "dashboard.html",
        subjects=subjects,
        study_hours=study_hours,
        tasks=tasks,
        cgpa=cgpa,
        study_tasks=study_tasks
    )


# =========================================================
# Task Routes
# =========================================================

@main.route("/add-task", methods=["GET", "POST"])
@login_required
def add_task():

    if request.method == "POST":

        title = request.form["title"].strip()

        # Prevent empty task titles
        if not title:
            flash(
                "Task title cannot be empty.",
                "warning"
            )

            return redirect(
                url_for("main.add_task")
            )

        # Create task for the logged-in user
        task = Task(
            title=title,
            completed=False,
            user_id=current_user.id
        )

        db.session.add(task)
        db.session.commit()

        flash(
            "Task created successfully.",
            "success"
        )

        return redirect(
            url_for("main.dashboard")
        )

    return render_template("add_task.html")


@main.route("/task/<int:id>/toggle", methods=["POST"])
@login_required
def toggle_task(id):

    task = get_user_task(id)

    task.completed = not task.completed

    db.session.commit()

    if task.completed:
        flash(
            "Task marked as complete.",
            "success"
        )
    else:
        flash(
            "Task marked as incomplete.",
            "info"
        )

    return redirect(
        url_for("main.dashboard")
    )


@main.route(
    "/task/<int:id>/edit",
    methods=["GET", "POST"]
)
@login_required
def edit_task(id):

    task = get_user_task(id)

    if request.method == "POST":

        title = request.form["title"].strip()

        if not title:
            flash(
                "Task title cannot be empty.",
                "warning"
            )

            return redirect(
                url_for(
                    "main.edit_task",
                    id=task.id
                )
            )

        task.title = title

        db.session.commit()

        flash(
            "Task updated successfully.",
            "success"
        )

        return redirect(
            url_for("main.dashboard")
        )

    return render_template(
        "edit_task.html",
        task=task
    )


@main.route(
    "/task/<int:id>/delete",
    methods=["POST"]
)
@login_required
def delete_task(id):

    task = get_user_task(id)

    db.session.delete(task)
    db.session.commit()

    flash(
        "Task deleted successfully.",
        "success"
    )

    return redirect(
        url_for("main.dashboard")
    )


# =========================================================
# Academic Routes
# =========================================================

@main.route("/academics")
@login_required
def academics():
    return render_template("academics.html")


@main.route("/cyberhub")
@login_required
def cyberhub():
    return render_template("cyberhub.html")


# =========================================================
# Account Routes
# =========================================================

@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@main.route("/settings")
@login_required
def settings():
    return render_template("settings.html")

@main.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()

        # Prevent empty fields
        if not username or not email:
            flash(
                "Username and email are required.",
                "warning"
            )
            return redirect(url_for("main.edit_profile"))

        # Check whether another user already has this username
        existing_username = User.query.filter(
            User.username == username,
            User.id != current_user.id
        ).first()

        if existing_username:
            flash(
                "That username is already taken.",
                "warning"
            )
            return redirect(url_for("main.edit_profile"))

        # Check whether another user already has this email
        existing_email = User.query.filter(
            User.email == email,
            User.id != current_user.id
        ).first()

        if existing_email:
            flash(
                "An account with that email already exists.",
                "warning"
            )
            return redirect(url_for("main.edit_profile"))

        # Update the logged-in user
        current_user.username = username
        current_user.email = email

        db.session.commit()

        flash(
            "Profile updated successfully.",
            "success"
        )

        return redirect(url_for("main.profile"))

    return render_template("edit_profile.html")