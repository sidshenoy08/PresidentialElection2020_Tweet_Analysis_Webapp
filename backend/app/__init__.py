from flask import Flask, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from app.config import Config
from app.db import init_db
from app.routes import register_routes
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)

    # Swagger UI setup
    SWAGGER_URL = "/docs"  # URL for Swagger UI
    API_URL = "/static/swagger.yaml"
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Serve Swagger YAML file
    @app.route("/static/swagger.yaml")
    def swagger_yaml():
        return send_from_directory("../static", "swagger.yaml")

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