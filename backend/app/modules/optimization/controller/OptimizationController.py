from flask import jsonify, request
from app.modules.optimization.service.OptimizationService import OptimizationService

class OptimizationController:

    @staticmethod
    def get_most_tweeted_about_by_user():
        data = OptimizationService.get_most_tweeted_about_by_user()
        return jsonify(data), 200
    
    @staticmethod
    def get_weekly_engagement_with_events():
        data_in = request.get_json()
        event_dates = data_in.get("event_dates", [])
        data = OptimizationService.get_weekly_engagement_with_events(event_dates)
        return jsonify(data), 200