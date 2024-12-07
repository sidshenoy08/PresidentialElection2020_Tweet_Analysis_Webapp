# from app.db import get_db
from app.db import db
from sqlalchemy import text
from app.models import Tweet, User
from datetime import datetime
from sqlalchemy import func, desc, asc
from flask import current_app

class HomepageRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_total_tweets_overview(start_date=None, end_date=None):
        sql = """
        SELECT
            COUNT(tweet_id) AS total_tweets,
            COUNT(DISTINCT user_id) AS unique_users
        FROM tweets
        WHERE tweet_about IS NOT NULL
        """
        params = {}
        if start_date:
            print(start_date)
            sql += " AND created_at >= :start_date"
            params["start_date"] = start_date
        if end_date:
            print(end_date)
            sql += " AND created_at <= :end_date"
            params["end_date"] = end_date

        with current_app.app_context():
            if not start_date and not end_date:
                result = db.session.execute(text(sql))
            else:
                print(sql)
                result = db.session.execute(text(sql), params)
            row = result.mappings().fetchone()
            return {
                "total_tweets": row["total_tweets"],
                "unique_users": row["unique_users"]
            }

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
        sort_order = "DESC" if order == "desc" else "ASC"
        sort_column = "tweet_count" if sort_by == "tweet_count" else "user_name"
        sql = text(f"""
        SELECT 
            t.user_id, 
            u.user_name, 
            COUNT(t.tweet_id) AS tweet_count
        FROM tweets t
        JOIN users u ON t.user_id = u.user_id
        GROUP BY t.user_id, u.user_name
        ORDER BY {sort_column} {sort_order}
        LIMIT :limit OFFSET :offset;
        """)
        params = {
            "limit": limit,
            "offset": offset
        }
        with current_app.app_context():
            result = db.session.execute(sql, params)
            return result.fetchall(), result.keys()
    
    @staticmethod
    def get_tweet_stats_by_candidate():
        sql = text("""
        SELECT
            tweet_about,
            COUNT(tweet_id) AS total_tweets, 
            SUM(retweet_count) AS total_retweets,
            SUM(likes) AS total_likes
        FROM tweets
        GROUP BY tweet_about;
        """)
        with current_app.app_context():
            result = db.session.execute(sql)
            return result.fetchall(), result.keys()
