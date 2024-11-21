from flask import jsonify, request
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
        limit = int(request.args.get("limit", 5))
        page = int(request.args.get("page", 1))
        sort_by = request.args.get("sort_by", "tweet_count")
        order = request.args.get("order", "desc")
        data = HomepageService.get_most_active_users(limit, page, sort_by, order)
        return jsonify(data), 200

