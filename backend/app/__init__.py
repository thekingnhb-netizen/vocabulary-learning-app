from flask import Flask
from flask_cors import CORS
from app.configuration.config import Config
from app.extensions import db, migrate
from app.routes import register_routes


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": app.config.get("CORS_ORIGINS", ["http://localhost:5173"])}})

    register_routes(app)

    with app.app_context():
        db.create_all()

    return app
