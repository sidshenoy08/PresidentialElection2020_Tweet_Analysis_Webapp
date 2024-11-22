from app.db import db
from sqlalchemy import text
from flask import current_app

class CandidateAnalysisRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_region_wise_engagement():
        sql = text("""
        WITH region_engagement AS (
            SELECT 
                l.country, 
                t.tweet_about, 
                SUM(t.likes + t.retweet_count) AS total_engagement
            FROM tweets t
            JOIN locations l ON t.lat = l.lat AND t.long = l.long
            GROUP BY l.country, t.tweet_about
        )
        SELECT 
            country,
            tweet_about,
            total_engagement,
            100.0 * total_engagement / SUM(total_engagement) OVER(PARTITION BY country) AS engagement_percentage
        FROM region_engagement
        ORDER BY country, engagement_percentage DESC;
        """)
        with current_app.app_context():
            result = db.session.execute(sql)
            return result.fetchall()

    @staticmethod
    def get_daily_trends(candidate):
        sql = """
        WITH daily_metrics AS (
            SELECT 
                CAST(t.created_at AS DATE) AS tweet_date,
                COUNT(t.tweet_id) AS tweet_count,
                SUM(t.likes + t.retweet_count) AS total_engagement
            FROM tweets t
            WHERE t.tweet_about = :candidate
            GROUP BY CAST(t.created_at AS DATE)
        )
        SELECT 
            tweet_date,
            tweet_count,
            total_engagement,
            AVG(total_engagement) OVER (
                ORDER BY tweet_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
            ) AS rolling_avg
        FROM daily_metrics
        ORDER BY tweet_date;
        """
        result = db.session.execute(sql, {"candidate": candidate})
        return result.fetchall()
    
    @staticmethod
    def get_weekly_comparison_with_events():
        sql = """
        WITH weekly_metrics AS (
            SELECT 
                DATE_TRUNC('week', t.created_at) AS week_start,
                t.tweet_about,
                COUNT(t.tweet_id) AS tweet_count,
                SUM(t.likes + t.retweet_count) AS total_engagement
            FROM tweets t
            GROUP BY DATE_TRUNC('week', t.created_at), t.tweet_about
        )
        SELECT 
            w.week_start,
            w.tweet_about,
            w.tweet_count,
            w.total_engagement,
            e.event_name,
            e.event_date
        FROM weekly_metrics w
        LEFT JOIN events e ON DATE_TRUNC('week', e.event_date) = w.week_start
        ORDER BY w.week_start, w.tweet_about;
        """
        result = db.session.execute(sql)
        return result.fetchall()

