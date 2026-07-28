from flask import Flask, render_template


def create_app():
    app = Flask(__name__)


    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/dashboard")
    def dashboard():

        subjects = 8
        study_hours = 0
        tasks = 12
        cgpa = 3.87

        study_tasks = [
        "Complete Algorithm Assignment",
        "Practice C++",
        "Finish TryHackMe Room",
        "Revise Vector Analysis"
        ]

        return render_template(
        "dashboard.html",
        subjects=subjects,
        study_hours=study_hours,
        tasks=tasks,
        cgpa=cgpa,
        study_tasks=study_tasks
    )


    @app.route("/academics")
    def academics():
        return render_template("academics.html")


    @app.route("/cyberhub")
    def cyberhub():
        return render_template("cyberhub.html")


    return app