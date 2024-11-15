from flask import jsonify
from app.modules.homepage.service.homepageService import HomepageService

class HomepageController:

    @staticmethod
    def get_total_tweets_overview():
        data = HomepageService.get_total_tweets_overview()
        return jsonify(data), 200

    @staticmethod
    def get_trending_candidates():
        data = HomepageService.get_trending_candidates()
        return jsonify(data), 200

    @staticmethod
    def get_most_active_users():
        data = HomepageService.get_most_active_users()
        return jsonify(data), 200
