from sqlalchemy.sql import text
from flask import current_app
from app.db import db

class OptimizationRepository:

    @staticmethod
    def get_most_tweeted_about_by_user():
        sql = text("""
            WITH trumpCountTable(user_id, total_trump_tweets, total_likes, total_retweets) AS (
                SELECT 
                    users.user_id, 
                    COUNT(tweets.tweet_id) AS total_trump_tweets, 
                    SUM(tweets.likes) AS total_likes, 
                    SUM(tweets.retweet_count) AS total_retweets
                FROM tweets 
                INNER JOIN users ON tweets.user_id = users.user_id
                WHERE tweets.tweet_about = 'Trump'
                GROUP BY users.user_id
            ),
            bidenCountTable(user_id, total_biden_tweets, total_likes, total_retweets) AS (
                SELECT 
                    users.user_id, 
                    COUNT(tweets.tweet_id) AS total_biden_tweets, 
                    SUM(tweets.likes) AS total_likes, 
                    SUM(tweets.retweet_count) AS total_retweets
                FROM tweets 
                INNER JOIN users ON tweets.user_id = users.user_id
                WHERE tweets.tweet_about = 'Biden'
                GROUP BY users.user_id
            )
            SELECT 
                users.user_id, 
                users.user_name,
                CASE 
                    WHEN trumpCountTable.total_trump_tweets > bidenCountTable.total_biden_tweets THEN 'Trump'
                    WHEN trumpCountTable.total_trump_tweets < bidenCountTable.total_biden_tweets THEN 'Biden'
                    ELSE 'Both'
                END AS most_tweeted_about,
                CASE 
                    WHEN trumpCountTable.total_trump_tweets > bidenCountTable.total_biden_tweets THEN trumpCountTable.total_likes
                    WHEN trumpCountTable.total_trump_tweets < bidenCountTable.total_biden_tweets THEN bidenCountTable.total_likes
                    ELSE trumpCountTable.total_likes + bidenCountTable.total_likes
                END AS total_likes,
                CASE 
                    WHEN trumpCountTable.total_trump_tweets > bidenCountTable.total_biden_tweets THEN trumpCountTable.total_retweets
                    WHEN trumpCountTable.total_trump_tweets < bidenCountTable.total_biden_tweets THEN bidenCountTable.total_retweets
                    ELSE trumpCountTable.total_retweets + bidenCountTable.total_retweets
                END AS total_retweets,
                users.user_followers_count, 
                users.user_join_date
            FROM users 
            INNER JOIN trumpCountTable ON users.user_id = trumpCountTable.user_id
            INNER JOIN bidenCountTable ON users.user_id = bidenCountTable.user_id;
        """)
        with current_app.app_context():
            result = db.session.execute(sql)
            return result.fetchall(), result.keys()
