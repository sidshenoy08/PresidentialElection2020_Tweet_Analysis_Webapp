from app.db import db
from app.models import Tweet
from sqlalchemy import func, desc, cast, Date, text
from flask import current_app
from decimal import Decimal

class EngagementTrendsRepository:
    def __init__(self):
        pass

    # This method is used to get the days where the engagement is higher than the average engagement by a certain threshold for a given candidate
    # The engagement is calculated by adding the number of likes and retweets for each tweet
    @staticmethod
    def get_engagement_spike_days(candidate, threshold=1.5, sort_by="date", order="asc"):
        sql = text(f"""
            WITH daily_engagement AS (
                SELECT 
                    CAST(created_at AS DATE) AS date,
                    SUM(likes + retweet_count) AS engagement
                FROM tweets
                WHERE tweet_about = :candidate
                GROUP BY CAST(created_at AS DATE)
            ),
            average_engagement AS (
                SELECT AVG(engagement) AS average
                FROM daily_engagement
            )
            SELECT 
                de.date, 
                de.engagement
            FROM daily_engagement de
            CROSS JOIN average_engagement ae
            WHERE de.engagement > ae.average * :threshold
            ORDER BY 
                { 'de.date' if sort_by == 'date' else 'de.engagement' } 
                { order };
        """)

        with current_app.app_context():
            result = db.session.execute(sql, {
                "candidate": candidate,
                "threshold": threshold
            })
            return result.fetchall(), result.keys()

    @staticmethod
    def get_daily_engagement(candidate):
        return (
            db.session.query(
                cast(Tweet.created_at, Date).label("date"),
                func.sum(Tweet.likes + Tweet.retweet_count).label("engagement")
            )
            .filter(Tweet.tweet_about == candidate)
            .group_by(cast(Tweet.created_at, Date))
            .order_by(cast(Tweet.created_at, Date))
            .all()
        )


    @staticmethod
    def get_high_volume_days(rank_limit=5, sort_by="engagement", order="desc"):
        sort_by = sort_by if sort_by in ["date", "engagement"] else "engagement"
        sort_column = "total_engagement" if sort_by == "engagement" else "tweet_date"
        order = "ASC" if order.lower() == "asc" else "DESC"

        sql = text(f"""
            WITH DailyCandidateVolume AS (
                SELECT
                    t.created_at::DATE AS tweet_date,
                    t.tweet_about AS candidate,
                    COUNT(t.tweet_id) AS tweet_count,
                    SUM(t.likes + t.retweet_count) AS total_engagement
                FROM tweets t
                WHERE t.tweet_about IN ('Biden', 'Trump')
                GROUP BY t.created_at::DATE, t.tweet_about
            ),
            HighVolumeDays AS (
                SELECT
                    candidate,
                    tweet_date,
                    tweet_count,
                    total_engagement,
                    RANK() OVER(PARTITION BY candidate ORDER BY tweet_count DESC) AS daily_rank
                FROM DailyCandidateVolume
            )
            SELECT
                tweet_date,
                candidate,
                tweet_count,
                total_engagement
            FROM HighVolumeDays
            WHERE daily_rank <= :rank_limit
            ORDER BY {sort_column} {order};
        """)

        with current_app.app_context():
            result = db.session.execute(sql, {"rank_limit": rank_limit})
            return result.fetchall(), result.keys()


    
    @staticmethod
    def get_weekly_sentiment_analysis(candidate, start_date, end_date):
        sql = text("""
            WITH weekly_data AS (
                SELECT 
                    DATE_TRUNC('week', t.created_at) AS week_start, 
                    COUNT(t.tweet_id) AS tweet_count,
                    SUM(CASE WHEN ts.sentiment = 'positive' THEN 1 ELSE 0 END) AS positive,
                    SUM(CASE WHEN ts.sentiment = 'negative' THEN 1 ELSE 0 END) AS negative,
                    SUM(CASE WHEN ts.sentiment = 'neutral' THEN 1 ELSE 0 END) AS neutral
                FROM tweets t
                JOIN tweet_sentiment ts ON t.tweet_id = ts.tweet_id
                WHERE t.tweet_about = :candidate 
                  AND t.created_at BETWEEN :start_date AND :end_date
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
