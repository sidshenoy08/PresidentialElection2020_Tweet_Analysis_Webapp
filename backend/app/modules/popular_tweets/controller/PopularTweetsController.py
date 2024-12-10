from flask import jsonify, request
from app.modules.popular_tweets.service.PopularTweetsService import PopularTweetsService

class PopularTweetsController:

    @staticmethod
    def get_top_tweets_by_retweets():
        try:
            candidate = request.args.get('candidate', 'Trump')
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            limit = int(request.args.get('limit', 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        data = PopularTweetsService.get_top_tweets_by_retweets(candidate, limit)
        return jsonify(data), 200

    @staticmethod
    def get_top_tweets_by_likes():
        try:
            candidate = request.args.get('candidate', 'Trump')
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            limit = int(request.args.get('limit', 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        data = PopularTweetsService.get_top_tweets_by_likes(candidate, limit)
        return jsonify(data), 200

    @staticmethod
    def get_tweet_location_insights():
        try:
            candidate = request.args.get('candidate', 'Trump')
            if(candidate not in {"Trump", "Biden"}):
                candidate = "Trump"
        except:
            candidate = "Trump"
        try:
            limit = int(request.args.get('limit', 10))
            if(limit <= 0):
                limit = 10
        except:
            limit = 10
        data = PopularTweetsService.get_tweet_location_insights(candidate, limit)
        return jsonify(data), 200
