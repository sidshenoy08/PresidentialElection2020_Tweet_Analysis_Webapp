from flask import jsonify, request
from app.modules.engagement_trends.service.EngagementTrendsService import EngagementTrendsService

class EngagementTrendsController:

    @staticmethod
    def get_engagement_spike_days():
        candidate = request.args.get('candidate', 'Trump')
        threshold = float(request.args.get('threshold', 1.5))
        sort_by = request.args.get("sort_by", "date")
        order = request.args.get("order", "desc")
        data = EngagementTrendsService.get_engagement_spike_days(candidate, threshold, sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_rolling_average_comparison():
        candidate = request.args.get('candidate', 'Trump')
        window = int(request.args.get('window', 7))
        sort_by = request.args.get("sort_by", "date")
        order = request.args.get("order", "desc")
        data = EngagementTrendsService.get_rolling_average_comparison(candidate, window, sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_high_volume_days():
        candidate = request.args.get('candidate', 'Trump')
        limit = int(request.args.get('limit', 5))
        sort_by = request.args.get("sort_by", "engagement")
        order = request.args.get("order", "desc")
        page = int(request.args.get('page', 1))
        data = EngagementTrendsService.get_high_volume_days(candidate, limit, page, sort_by, order)
        return jsonify(data), 200
