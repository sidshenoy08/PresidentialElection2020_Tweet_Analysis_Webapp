# from app.db import get_db
from app.db import db
# from sqlalchemy import text
from app.models import Tweet, User
from datetime import datetime
from sqlalchemy import func, desc, asc

class HomepageRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_total_tweets_overview(start_date=None, end_date=None):
        total_tweets_query = db.session.query(func.count(Tweet.tweet_id)).filter(Tweet.tweet_about.isnot(None))
        if start_date:
            total_tweets_query = total_tweets_query.filter(Tweet.created_at >= start_date)
        if end_date:
            total_tweets_query = total_tweets_query.filter(Tweet.created_at <= end_date)
        total_tweets = total_tweets_query.scalar()

        unique_users_query = db.session.query(func.count(func.distinct(Tweet.user_id))).filter(Tweet.tweet_about.isnot(None))
        if start_date:
            unique_users_query = unique_users_query.filter(Tweet.created_at >= start_date)
        if end_date:
            unique_users_query = unique_users_query.filter(Tweet.created_at <= end_date)
        unique_users = unique_users_query.scalar()

        return {'total_tweets': total_tweets, 'unique_users': unique_users}

    

    @staticmethod
    def get_trending_candidates(limit=5, sort_by="tweet_count", order="desc"):
        sort_order = desc if order == "desc" else asc
        sort_column = Tweet.tweet_about if sort_by == "candidate" else func.count(Tweet.tweet_id)
        res = (
            db.session.query(Tweet.tweet_about, func.count(Tweet.tweet_id).label('tweet_count'))
            .filter(Tweet.tweet_about.isnot(None))
            .group_by(Tweet.tweet_about)
            .order_by(sort_order(sort_column))
            .limit(limit)
            .all()
        )
        return res

    @staticmethod
    def get_most_active_users(limit=5, offset=0, sort_by="tweet_count", order="desc"):
        sort_order = desc if order == "desc" else asc
        sort_column = func.count(Tweet.tweet_id) if sort_by == "tweet_count" else User.user_name
        res = (
            db.session.query(Tweet.user_id, User.user_name, func.count(Tweet.tweet_id).label('tweet_count'))
            .join(User, Tweet.user_id == User.user_id)
            .group_by(Tweet.user_id, User.user_name)
            .order_by(sort_order(sort_column))
            .offset(offset)
            .limit(limit)
            .all()
        )
        return res

