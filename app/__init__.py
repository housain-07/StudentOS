from flask import Flask, render_template


def create_app():
    app = Flask(__name__)


    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")


    @app.route("/academics")
    def academics():
        return render_template("academics.html")


    @app.route("/cyberhub")
    def cyberhub():
        return render_template("cyberhub.html")


    return app