from flask import jsonify, request
from app.modules.popular_tweets.service.PopularTweetsService import PopularTweetsService

class PopularTweetsController:

    @staticmethod
    def get_top_tweets_by_retweets():
        candidate = request.args.get('candidate', 'Trump')
        limit = int(request.args.get('limit', 10))
        data = PopularTweetsService.get_top_tweets_by_retweets(candidate, limit)
        return jsonify(data), 200

    @staticmethod
    def get_top_tweets_by_likes():
        candidate = request.args.get('candidate', 'Trump')
        limit = int(request.args.get('limit', 10))
        data = PopularTweetsService.get_top_tweets_by_likes(candidate, limit)
        return jsonify(data), 200

    @staticmethod
    def get_tweet_location_insights():
        candidate = request.args.get('candidate', 'Trump')
        limit = int(request.args.get('limit', 10))
        data = PopularTweetsService.get_tweet_location_insights(candidate, limit)
        return jsonify(data), 200
