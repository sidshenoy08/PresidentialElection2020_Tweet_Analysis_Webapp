from flask import jsonify, request
from app.modules.homepage.service.homepageService import HomepageService

class HomepageController:

    @staticmethod
    def get_total_tweets_overview():
        start_date_str = request.args.get('start_date') 
        end_date_str = request.args.get('end_date') 
        data = HomepageService.get_total_tweets_overview(start_date_str, end_date_str)
        return jsonify(data), 200

    @staticmethod
    def get_trending_candidates():
        sort_by = request.args.get("sort_by", "tweet_count")
        order = request.args.get("order", "desc")
        data = HomepageService.get_trending_candidates(limit=5, sort_by=sort_by, order=order)
        return jsonify(data), 200

    @staticmethod
    def get_most_active_users():
        limit = int(request.args.get("limit", 5))
        page = int(request.args.get("page", 1))
        sort_by = request.args.get("sort_by", "tweet_count")
        order = request.args.get("order", "desc")
        data = HomepageService.get_most_active_users(limit, page, sort_by, order)
        return jsonify(data), 200
    
    @staticmethod
    def get_tweet_stats_by_candidate():
        data = HomepageService.get_tweet_stats_by_candidate()
        return jsonify(data), 200