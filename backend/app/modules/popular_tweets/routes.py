from flask import Blueprint
from app.modules.popular_tweets.controller.PopularTweetsController import PopularTweetsController

popular_tweets_bp = Blueprint('popular-tweets', __name__)

popular_tweets_bp.route('/retweets', methods=['GET'])(PopularTweetsController.get_top_tweets_by_retweets)
popular_tweets_bp.route('/likes', methods=['GET'])(PopularTweetsController.get_top_tweets_by_likes)
popular_tweets_bp.route('/location-insights', methods=['GET'])(PopularTweetsController.get_tweet_location_insights)