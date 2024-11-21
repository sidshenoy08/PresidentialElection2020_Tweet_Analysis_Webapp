from flask import Blueprint
from app.modules.user_engagement.controller.UserEngagementController import UserEngagementController

user_engagement_bp = Blueprint('user-engagement-bp', __name__)

user_engagement_bp.route('/top-users', methods=['GET'])(UserEngagementController.get_top_users_by_engagement)
user_engagement_bp.route('/activity-breakdown', methods=['GET'])(UserEngagementController.get_user_activity_breakdown)
user_engagement_bp.route('/popular-tweets', methods=['POST'])(UserEngagementController.get_popular_tweets_by_users)