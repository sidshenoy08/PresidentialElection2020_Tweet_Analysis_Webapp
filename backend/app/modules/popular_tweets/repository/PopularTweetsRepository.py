from app.db import db
from flask import current_app
from app.models import Tweet, User, Location
from sqlalchemy import func, desc

class PopularTweetsRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_top_tweets_by_retweets(candidate, limit=10):
        return (
            db.session.query(Tweet.tweet_id, Tweet.tweet, Tweet.retweet_count, Tweet.likes, User.user_name, Location.city, Location.state)
            .join(User, Tweet.user_id == User.user_id)
            .join(Location, (Tweet.lat == Location.lat) & (Tweet.long == Location.long))
            .filter(Tweet.tweet_about == candidate)
            .order_by(desc(Tweet.retweet_count))
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_top_tweets_by_likes(candidate, limit=10):
        return (
            db.session.query(Tweet.tweet_id, Tweet.tweet, Tweet.likes, Tweet.retweet_count, User.user_name, Location.city, Location.state)
            .join(User, Tweet.user_id == User.user_id)
            .join(Location, (Tweet.lat == Location.lat) & (Tweet.long == Location.long))
            .filter(Tweet.tweet_about == candidate)
            .order_by(desc(Tweet.likes))
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_tweet_location_insights(candidate, limit=10):
        return (
            db.session.query(Location.city, Location.state, func.count(Tweet.tweet_id).label('tweet_count'))
            .join(Tweet, (Location.lat == Tweet.lat) & (Location.long == Tweet.long))
            .filter(Tweet.tweet_about == candidate)
            .group_by(Location.city, Location.state)
            .order_by(desc('tweet_count'))
            .limit(limit)
            .all()
        )
