from flask import jsonify, request
from app.modules.geographic_analysis.service.GeographicAnalysisService import GeographicAnalysisService

class GeographicAnalysisController:
    @staticmethod
    def get_most_tweets_by_country():
        # limit = int(request.args.get("limit", 10))
        sort_by = request.args.get("sort_by", "tweet_count")
        order = request.args.get("order", "DESC").upper()
        data = GeographicAnalysisService.get_most_tweets_by_country(sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_city_level_analysis():
        try:
            limit = int(request.args.get("limit", 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        try:
            sort_by = request.args.get("sort_by", "tweet_count")
            if(sort_by not in {"city", "tweet_count", "likes", "retweets"}):
                sort_by = "tweet_count"
        except:
            sort_by = "tweet_count"
        try:
            order = request.args.get("order", "DESC").upper()
            if(order not in {"ASC", "DESC"}):
                order = "DESC"
        except:
            order = "DESC"
        print(limit, order, sort_by)
        data = GeographicAnalysisService.get_city_level_analysis(limit, sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_top_tweets_by_region():
        filters = {
            "continent": request.args.get("continent") if((request.args.get("continent") != 'undefined') and (request.args.get("continent") != '')) else None,
            "country": request.args.get("country") if((request.args.get("country") != 'undefined') and (request.args.get("country") != '')) else None,
            "state": request.args.get("state") if((request.args.get("state") != 'undefined') and (request.args.get("state") != '')) else None,
            "city": request.args.get("city") if((request.args.get("city") != 'undefined') and (request.args.get("city") != '')) else None
        }
        try:
            sort_by = request.args.get("sort_by", "likes")
            if(sort_by not in {"tweet_id", "retweet_count", "likes"}):
                sort_by = "likes"
        except:
            sort_by = "likes"
        try:
            order = request.args.get("order", "DESC").upper()
            if(order not in {"ASC", "DESC"}):
                order = "DESC"
        except:
            order = "DESC"
        try:
            limit = int(request.args.get("limit", 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        data = GeographicAnalysisService.get_top_tweets_by_region(filters, sort_by, order, limit)
        return jsonify(data), 200
    
    @staticmethod
    def get_engagement_by_timezone():
        try:
            candidate = request.args.get("candidate", "Trump")
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        # sort_by = request.args.get("sort_by", "tweet_count")
        # order = request.args.get("order", "DESC").upper()
        # limit = int(request.args.get("limit", 10))
        data = GeographicAnalysisService.get_engagement_by_timezone(candidate)
        return jsonify(data), 200