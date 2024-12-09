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
        
    @staticmethod
    def get_weekly_engagement_with_events(event_dates):
        sql = text("""
            WITH WeeklyEngagement AS (
                SELECT
                    DATE_TRUNC('week', t.created_at) AS tweet_week,
                    t.tweet_about AS candidate,
                    COUNT(t.tweet_id) AS weekly_tweet_count,
                    SUM(t.likes + t.retweet_count) AS weekly_engagement
                FROM tweets t
                GROUP BY DATE_TRUNC('week', t.created_at), t.tweet_about
            ),
            EventDays AS (
                SELECT
                    t.created_at::DATE AS event_date,
                    t.tweet_about AS candidate,
                    COUNT(t.tweet_id) AS event_tweet_count,
                    SUM(t.likes + t.retweet_count) AS event_engagement
                FROM tweets t
                WHERE t.created_at::DATE = ANY(:event_dates)
                GROUP BY t.created_at::DATE, t.tweet_about
            )
            SELECT
                w.tweet_week,
                w.candidate,
                w.weekly_tweet_count,
                w.weekly_engagement,
                e.event_date,
                e.event_tweet_count,
                e.event_engagement
            FROM WeeklyEngagement w
            LEFT JOIN EventDays e 
                ON DATE_TRUNC('week', e.event_date) = w.tweet_week 
                AND e.candidate = w.candidate
            ORDER BY w.candidate, w.tweet_week;
        """)
        with current_app.app_context():
            result = db.session.execute(sql, {"event_dates": event_dates})
            return result.fetchall(), result.keys()