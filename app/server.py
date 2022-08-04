from flask import Flask
from flask_restx import Api

from app.views import start_bp, fight_bp

# Initiate Api
api = Api(title="SkyWars", doc="/docs")


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    # Register blueprints
    app.register_blueprint(start_bp)
    app.register_blueprint(fight_bp)

    return app
