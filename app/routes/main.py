from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

from app import db
from app.models.task import Task

main = Blueprint("main", __name__)


def get_user_task(task_id):
    """
    Retrieve a task that belongs to the currently logged-in user.

    Returns:
        Task: The requested task.

    Raises:
        404: If the task does not exist.
        403: If the task belongs to another user.
    """

    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        abort(403)

    return task


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/dashboard")
@login_required
def dashboard():

    subjects = 8
    study_hours = 0
    cgpa = 3.87

    # Only show tasks belonging to the logged-in user
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


@main.route("/add-task", methods=["GET", "POST"])
@login_required
def add_task():

    if request.method == "POST":

        title = request.form["title"].strip()

        if title:

            task = Task(
                title=title,
                completed=False,
                user_id=current_user.id
            )

            db.session.add(task)
            db.session.commit()

        return redirect(url_for("main.dashboard"))

    return render_template("add_task.html")


@main.route("/task/<int:id>/toggle")
@login_required
def toggle_task(id):

    task = get_user_task(id)

    task.completed = not task.completed

    db.session.commit()

    return redirect(url_for("main.dashboard"))


@main.route("/task/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(id):

    task = get_user_task(id)

    if request.method == "POST":

        title = request.form["title"].strip()

        if title:
            task.title = title
            db.session.commit()

        return redirect(url_for("main.dashboard"))

    return render_template(
        "edit_task.html",
        task=task
    )


@main.route("/task/<int:id>/delete")
@login_required
def delete_task(id):

    task = get_user_task(id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("main.dashboard"))


@main.route("/academics")
@login_required
def academics():
    return render_template("academics.html")


@main.route("/cyberhub")
@login_required
def cyberhub():
    return render_template("cyberhub.html")