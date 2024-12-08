from flask import Blueprint
from app.modules.engagement_trends.controller.EngagementTrendsController import EngagementTrendsController

engagement_trends_bp = Blueprint('engagement_trends_bp', __name__)

engagement_trends_bp.route('/spikes', methods=['GET'])(EngagementTrendsController.get_engagement_spike_days)
engagement_trends_bp.route('/rolling-average', methods=['GET'])(EngagementTrendsController.get_rolling_average_comparison)
engagement_trends_bp.route('/high-volume-days', methods=['GET'])(EngagementTrendsController.get_high_volume_days)
engagement_trends_bp.route('/weekly-sentiment', methods=['GET'])(EngagementTrendsController.get_weekly_sentiment_analysis)