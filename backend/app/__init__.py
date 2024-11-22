from flask import Flask, jsonify
from app.config import Config
from app.db import init_db
from app.routes import register_routes
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    register_routes(app)
    register_error_handlers(app)
    return app

# Global error handler function
def register_error_handlers(app):
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        return jsonify({"error": str(e)}), 400

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500