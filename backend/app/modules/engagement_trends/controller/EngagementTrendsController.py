from flask import jsonify, request
from app.modules.engagement_trends.service.EngagementTrendsService import EngagementTrendsService

class EngagementTrendsController:

    @staticmethod
    def get_engagement_spike_days():
        try:
            candidate = request.args.get('candidate', 'Trump')
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            threshold = float(request.args.get('threshold', 1.5))
            if(threshold <= 0):
                threshold = 1.5
        except:
            threshold = 1.5
        try:
            sort_by = request.args.get("sort_by", "date")
            if(sort_by not in {"date", "engagement"}):
                sort_by = "date"
        except:
            sort_by = "date"
        try:
            order = request.args.get("order", "desc")
            if(order not in {"asc", "desc"}):
                order = "desc"
        except:
            order = "desc"
        data = EngagementTrendsService.get_engagement_spike_days(candidate, threshold, sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_rolling_average_comparison():
        try:
            candidate = request.args.get('candidate', 'Trump')
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            window = int(request.args.get('window', 7))
            if(window <= 0):
                window = 7
        except:
            window = 7
        try:
            sort_by = request.args.get("sort_by", "date")
            if(sort_by not in {"date", "engagement", "rolling_avg"}):
                sort_by = "date"
        except:
            sort_by = "date"
        try:
            order = request.args.get("order", "desc")
            if(order not in {"asc", "desc"}):
                order = "desc"
        except:
            order = "desc"
        data = EngagementTrendsService.get_rolling_average_comparison(candidate, window, sort_by, order)
        return jsonify(data), 200

    @staticmethod
    def get_high_volume_days():
        try:
            candidate = request.args.get('candidate', 'Trump')
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            limit = int(request.args.get('limit', 5))
            if(limit <= 0):
                limit = 5
        except:
            limit = 5
        try:
            sort_by = request.args.get("sort_by", "engagement")
            if(sort_by not in {"date", "engagement"}):
                sort_by = "engagement"
        except:
            sort_by = "engagement"
        try:
            order = request.args.get("order", "desc")
            if(order not in {"asc", "desc"}):
                order = "desc"
        except:
            order = "desc"
        try:
            page = int(request.args.get('page', 1))
            if(page <= 0):
                page = 1
        except:
            page = 1
        data = EngagementTrendsService.get_high_volume_days(candidate, limit, page, sort_by, order)
        return jsonify(data), 200
    
    @staticmethod
    def get_weekly_sentiment_analysis():
        candidate = request.args.get("candidate", "Trump")
        start_date = '2020-10-15'
        end_date = '2020-11-08'
        data = EngagementTrendsService.get_weekly_sentiment_analysis(candidate, start_date, end_date)
        return jsonify(data), 200