from flask import Blueprint
from app.modules.optimization.controller.OptimizationController import OptimizationController

optimization_bp = Blueprint('optimization_bp', __name__)

optimization_bp.route('/most-tweeted-about', methods=['GET'])(OptimizationController.get_most_tweeted_about_by_user)
optimization_bp.route('/weekly-engagement-with-events', methods=['POST'])(OptimizationController.get_weekly_engagement_with_events)