from flask import Flask
from app.modules.homepage.routes import homepage_bp

def register_routes(app: Flask):
    app.register_blueprint(homepage_bp, url_prefix='/api/homepage')