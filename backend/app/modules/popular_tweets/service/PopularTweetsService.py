from app.modules.popular_tweets.repository.PopularTweetsRepository import PopularTweetsRepository

class PopularTweetsService:

    @staticmethod
    def get_top_tweets_by_retweets(candidate, limit=10):
        tweets = PopularTweetsRepository.get_top_tweets_by_retweets(candidate, limit)
        return [row._asdict() for row in tweets]

    @staticmethod
    def get_top_tweets_by_likes(candidate, limit=10):
        tweets = PopularTweetsRepository.get_top_tweets_by_likes(candidate, limit)
        return [row._asdict() for row in tweets]

    @staticmethod
    def get_tweet_location_insights(candidate, limit=10):
        locations = PopularTweetsRepository.get_tweet_location_insights(candidate, limit)
        return [row._asdict() for row in locations]
