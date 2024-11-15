# from app.db import get_db
from app.db import db
# from sqlalchemy import text
from app.models import Tweet, User
from sqlalchemy import func

class HomepageRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_total_tweets_overview():
        total_tweets = db.session.query(func.count(Tweet.tweet_id)).scalar()
        unique_users = db.session.query(func.count(func.distinct(Tweet.user_id))).scalar()
        return {
            'total_tweets': total_tweets,
            'unique_users': unique_users
        }
    

    @staticmethod
    def get_trending_candidates(limit=5):
        res = (
            db.session.query(Tweet.tweet_about, func.count(Tweet.tweet_id).label('tweet_count'))
            .filter(Tweet.tweet_about.isnot(None))
            .group_by(Tweet.tweet_about)
            .order_by(db.desc('tweet_count'))
            .limit(limit)
            .all()
        )
        return res

    @staticmethod
    def get_most_active_users(limit=5):
        res = (
            db.session.query(Tweet.user_id, User.user_name, func.count(Tweet.tweet_id).label('tweet_count'))
            .join(User, Tweet.user_id == User.user_id)
            .group_by(Tweet.user_id, User.user_name)
            .order_by(db.desc('tweet_count'))
            .limit(limit)
            .all()
        )
        return res

