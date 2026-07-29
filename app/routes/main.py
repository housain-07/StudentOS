from flask import Blueprint, render_template, request, redirect, url_for

from app.models.task import Task
from app import db

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")

@main.route("/create-task")
def create_task():

    task = Task(
        title="Complete Algorithms Assignment",
        completed=False
    )

    db.session.add(task)
    db.session.commit()

    return "Task Created Successfully!"

@main.route("/add-task", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        title = request.form["title"]

        task = Task(
            title=title,
            completed=False
        )

        db.session.add(task)
        db.session.commit()

        return redirect(url_for("main.dashboard"))

    return render_template("add_task.html")

@main.route("/dashboard")
def dashboard():

    subjects = 8
    study_hours = 0
    cgpa = 3.87


    tasks = Task.query.count()
    study_tasks = Task.query.all()

    return render_template(
        "dashboard.html",
        subjects=subjects,
        study_hours=study_hours,
        tasks=tasks,
        cgpa=cgpa,
        study_tasks=study_tasks
    )


@main.route("/academics")
def academics():
    return render_template("academics.html")


@main.route("/cyberhub")
def cyberhub():
    return render_template("cyberhub.html")