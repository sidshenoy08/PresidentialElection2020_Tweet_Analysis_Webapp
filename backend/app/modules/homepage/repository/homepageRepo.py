# from app.db import get_db
from app.db import db
# from sqlalchemy import text
from app.models import Tweet
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
        query = """
        SELECT candidate, COUNT(*) AS tweet_count
        FROM tweets
        WHERE candidate IS NOT NULL
        GROUP BY candidate
        ORDER BY tweet_count DESC
        LIMIT %s;
        """
        db = get_db()
        res = db.execute(query, (limit,)).fetchall()
        return res

    @staticmethod
    def get_most_active_users(limit=5):
        query = """
        SELECT user_id, username, COUNT(*) AS tweet_count
        FROM tweets
        GROUP BY user_id, username
        ORDER BY tweet_count DESC
        LIMIT %s;
        """
        db = get_db()
        res = db.execute(query, (limit,)).fetchall()
        return res
