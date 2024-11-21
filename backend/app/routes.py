from flask import Flask
from app.modules.homepage.routes import homepage_bp
from app.modules.popular_tweets.routes import popular_tweets_bp
from app.modules.engagement_trends.routes import engagement_trends_bp
from app.modules.user_engagement.routes import user_engagement_bp

def register_routes(app: Flask):
    app.register_blueprint(homepage_bp, url_prefix='/api/homepage')
    app.register_blueprint(popular_tweets_bp, url_prefix='/api/popular-tweets')
    app.register_blueprint(engagement_trends_bp, url_prefix='/api/engagement-trends')
    app.register_blueprint(user_engagement_bp, url_prefix='/api/user-engagement')