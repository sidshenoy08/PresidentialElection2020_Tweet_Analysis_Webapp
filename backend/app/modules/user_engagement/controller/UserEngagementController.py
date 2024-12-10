from flask import jsonify, request
from app.modules.user_engagement.service.UserEngagementService import UserEngagementService

class UserEngagementController:
    @staticmethod
    def get_top_users_by_engagement():
        # try-except blocks to handle incorrect or blank query parameters
        try:
            order = request.args.get("order", "desc")
            if(order not in {"asc", "desc"}):
                order = "desc"
        except:
            order = "desc"
        try:
            limit = int(request.args.get("limit", 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        data = UserEngagementService.get_top_users_by_engagement(order, limit)
        return jsonify(data), 200

    @staticmethod
    def get_user_activity_breakdown():
        # try-except blocks to handle incorrect or blank query parameters
        try:
            candidate = request.args.get("candidate", "Trump")
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            order = request.args.get("order", "desc")
            if(order not in {"asc", "desc"}):
                order = "desc"
        except:
            order = "desc"
        try:
            limit = int(request.args.get("limit", 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        data = UserEngagementService.get_user_activity_breakdown(candidate, order, limit)
        return jsonify(data), 200

    @staticmethod
    def get_popular_tweets_by_users():
        dataIn = request.get_json()
        user_ids = dataIn.get("user_ids", [])
        order = dataIn.get("order", "desc")
        by = dataIn.get("by", "total_engagement")
        data = UserEngagementService.get_popular_tweets_by_users(user_ids, order, by)
        return jsonify(data), 200
    
      
    @staticmethod
    def get_influential_users():
        # try-except blocks to handle incorrect or blank query parameters
        try:
            candidate = request.args.get("candidate", "Trump")
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            limit = int(request.args.get("limit", 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        data = UserEngagementService.get_influential_users(candidate, limit)
        return jsonify(data), 200