from flask import jsonify, request
from app.modules.geographic_analysis.service.GeographicAnalysisService import GeographicAnalysisService

class GeographicAnalysisController:
    @staticmethod
    def get_most_tweets_by_country():
        limit = int(request.args.get("limit", 10))
        sort_by = request.args.get("sort_by", "tweet_count")
        order = request.args.get("order", "DESC").upper()
        data = GeographicAnalysisService.get_most_tweets_by_country(limit, sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_city_level_analysis():
        limit = int(request.args.get("limit", 10))
        sort_by = request.args.get("sort_by", "tweet_count")
        order = request.args.get("order", "DESC").upper()
        data = GeographicAnalysisService.get_city_level_analysis(limit, sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_top_tweets_by_region():
        filters = {
            "continent": request.args.get("continent"),
            "country": request.args.get("country"),
            "state": request.args.get("state"),
            "city": request.args.get("city"),
        }
        sort_by = request.args.get("sort_by", "likes")
        order = request.args.get("order", "DESC").upper()
        limit = int(request.args.get("limit", 10))
        data = GeographicAnalysisService.get_top_tweets_by_region(filters, sort_by, order, limit)
        return jsonify(data), 200
    
    @staticmethod
    def get_engagement_by_timezone():
        candidate = request.args.get("candidate", "Trump")
        sort_by = request.args.get("sort_by", "tweet_count")
        order = request.args.get("order", "DESC").upper()
        limit = int(request.args.get("limit", 10))
        data = GeographicAnalysisService.get_engagement_by_timezone(candidate, sort_by, order, limit)
        return jsonify(data), 200