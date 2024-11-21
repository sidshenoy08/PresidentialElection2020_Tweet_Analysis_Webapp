from flask import jsonify, request
from app.modules.user_engagement.service.UserEngagementService import UserEngagementService

class UserEngagementController:
    @staticmethod
    def get_top_users_by_engagement():
        order = request.args.get("order", "desc")
        limit = int(request.args.get("limit", 10))
        data = UserEngagementService.get_top_users_by_engagement(order, limit)
        return jsonify(data), 200

    @staticmethod
    def get_user_activity_breakdown():
        candidate = request.args.get("candidate", "Trump")
        order = request.args.get("order", "desc")
        limit = int(request.args.get("limit", 10))
        data = UserEngagementService.get_user_activity_breakdown(candidate, order, limit)
        return jsonify(data), 200

    @staticmethod
    def get_popular_tweets_by_users():
        dataIn = request.get_json()
        user_ids = dataIn.get("user_ids", [])
        order = dataIn.get("order", "desc")
        by = dataIn.get("by", "total_engagement")
        limit = int(dataIn.get("limit", 10))
        data = UserEngagementService.get_popular_tweets_by_users(user_ids, order, limit, by)
        return jsonify(data), 200
