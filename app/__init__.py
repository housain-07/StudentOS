from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

# Extensions
db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    # Lazy import to avoid circular imports
    from app.models.user import User
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Import models so SQLAlchemy knows about them
    from . import models

    # Import and register blueprints
    from .routes.main import main
    from .routes.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app