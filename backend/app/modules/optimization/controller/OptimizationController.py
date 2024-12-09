from flask import jsonify
from app.modules.optimization.service.OptimizationService import OptimizationService

class OptimizationController:

    @staticmethod
    def get_most_tweeted_about_by_user():
        data = OptimizationService.get_most_tweeted_about_by_user()
        return jsonify(data), 200
    
    @staticmethod
    def get_weekly_engagement_with_events():
        event_dates = request.args.getlist('event_dates')  # Example: ["2020-10-22", "2020-11-03"]
        data = OptimizationService.get_weekly_engagement_with_events(event_dates)
        return jsonify(data), 200