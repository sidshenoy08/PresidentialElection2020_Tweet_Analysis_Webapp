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
        daily_engagement = (
            db.session.query(
                cast(Tweet.created_at, Date).label('date'),
                func.sum(Tweet.likes + Tweet.retweet_count).label('engagement')
            )
            .filter(Tweet.tweet_about == candidate)
            .group_by(cast(Tweet.created_at, Date))
            .subquery()
        )

        average_engagement = db.session.query(
            func.avg(daily_engagement.c.engagement).label('average')
        ).scalar()
        
        order_by = daily_engagement.c.date if sort_by == "date" else daily_engagement.c.engagement
        spikes = (
            db.session.query(daily_engagement.c.date, daily_engagement.c.engagement)
            .filter(daily_engagement.c.engagement > average_engagement * Decimal(threshold))
            .order_by(order_by if order == "asc" else desc(order_by))
            .all()
        )
        return spikes

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
    def get_high_volume_days(candidate, limit=5, sort_by="engagement", order="desc"):
        order_by = cast(Tweet.created_at, Date) if sort_by == "date" else 'engagement'
        ord = desc(order_by) if order == "desc" else order_by

        res = (
            db.session.query(
                cast(Tweet.created_at, Date).label('date'),
                func.sum(Tweet.likes + Tweet.retweet_count).label('engagement')
            )
            .filter(Tweet.tweet_about == candidate)
            .group_by(cast(Tweet.created_at, Date))
            .order_by(ord)
            .limit(limit)
            .all()
        )
        return res
    
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
