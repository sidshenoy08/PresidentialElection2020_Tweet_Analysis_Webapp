from sqlalchemy.sql import text
from app.db import db
from flask import current_app

class GeographicAnalysisRepository:
    @staticmethod
    def get_most_tweets_by_country(limit, sort_by, order):
        sql = text(f"""
            SELECT 
                l.country, 
                COUNT(t.tweet_id) AS tweet_count
            FROM tweets t
            JOIN locations l ON t.lat = l.lat AND t.long = l.long
            GROUP BY l.country
            ORDER BY {sort_by} {order}
            LIMIT :limit;
        """)
        with current_app.app_context():
            result = db.session.execute(sql, {"limit": limit})
            return result.fetchall(), result.keys()

    @staticmethod
    def get_city_level_analysis(limit, sort_by, order):
        sql = text(f"""
            SELECT 
                l.city, 
                COUNT(t.tweet_id) AS tweet_count,
                SUM(t.likes) AS likes,
                SUM(t.retweet_count) AS retweets
            FROM tweets t
            JOIN locations l ON t.lat = l.lat AND t.long = l.long
            GROUP BY l.city
            ORDER BY {sort_by} {order}
            LIMIT :limit;
        """)
        with current_app.app_context():
            result = db.session.execute(sql, {"limit": limit})
            return result.fetchall(), result.keys()

    @staticmethod
    def get_top_tweets_by_region(filters, sort_by, order, limit):
        sql = text(f"""
            SELECT 
                t.tweet_id, 
                t.tweet, 
                t.likes, 
                t.retweet_count, 
                u.user_name, 
                CONCAT(l.city, ', ', l.state, ', ', l.country) AS location
            FROM tweets t
            JOIN users u ON t.user_id = u.user_id
            JOIN locations l ON t.lat = l.lat AND t.long = l.long
            WHERE 
                (:continent IS NULL OR l.continent = :continent) AND
                (:country IS NULL OR l.country = :country) AND
                (:state IS NULL OR l.state = :state) AND
                (:city IS NULL OR l.city = :city)
            ORDER BY {sort_by} {order}
            LIMIT :limit;
        """)
        with current_app.app_context():
            result = db.session.execute(sql, {
                "continent": filters.get("continent"),
                "country": filters.get("country"),
                "state": filters.get("state"),
                "city": filters.get("city"),
                "limit": limit
            })
            return result.fetchall(), result.keys()
        
    @staticmethod
    def get_weekly_sentiment_analysis(candidate, start_date, end_date):
        sql = text(f"""
            WITH weekly_data AS (
                SELECT 
                    DATE_TRUNC('week', t.created_at) AS week_start, 
                    COUNT(t.tweet_id) AS tweet_count,
                    SUM(CASE WHEN sentiment = 'positive' THEN 1 ELSE 0 END) AS positive,
                    SUM(CASE WHEN sentiment = 'negative' THEN 1 ELSE 0 END) AS negative,
                    SUM(CASE WHEN sentiment = 'neutral' THEN 1 ELSE 0 END) AS neutral
                FROM tweets t
                WHERE t.tweet_about = :candidate AND t.created_at BETWEEN :start_date AND :end_date
                GROUP BY DATE_TRUNC('week', t.created_at)
            )
            SELECT * FROM weekly_data
            ORDER BY week_start;
        """)
        with current_app.app_context():
            result = db.session.execute(sql, {
                "candidate": candidate,
                "start_date": start_date,
                "end_date": end_date
            })
            return result.fetchall(), result.keys()
