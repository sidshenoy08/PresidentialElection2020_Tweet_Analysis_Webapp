from flask import jsonify
from app.modules.optimization.service.OptimizationService import OptimizationService

class OptimizationController:

    @staticmethod
    def get_most_tweeted_about_by_user():
        data = OptimizationService.get_most_tweeted_about_by_user()
        return jsonify(data), 200