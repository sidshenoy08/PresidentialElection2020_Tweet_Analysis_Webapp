from app.db import db
from app.models import Tweet, User
from sqlalchemy import func, desc, asc, case, text
from flask import current_app

class UserEngagementRepository:
    @staticmethod
    def get_top_users_by_engagement(sort_order, limit=10):
        return (
            db.session.query(
                User.user_id,
                User.user_name,
                User.user_screen_name,
                func.sum(Tweet.likes + Tweet.retweet_count).label("total_engagement"),
                # TODO: Add condition to check if total_engagement is > 0
                case(
                    (User.user_followers_count > 0, 
                     func.sum(Tweet.likes + Tweet.retweet_count) / func.max(User.user_followers_count)),
                    else_=0
                ).label("engagement_to_followers_ratio"),
                func.max(User.user_followers_count).label("followers")
            )
            .join(Tweet, Tweet.user_id == User.user_id)
            .group_by(User.user_id, User.user_name, User.user_screen_name)
            .order_by(sort_order("total_engagement"))
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_user_activity_breakdown(candidate, sort_order, limit=10):
        return (
            db.session.query(
                User.user_id,
                User.user_name,
                User.user_screen_name,
                func.sum(Tweet.likes + Tweet.retweet_count).label("total_engagement"),
                func.count(Tweet.tweet_id).label("tweet_count")
            )
            .join(Tweet, Tweet.user_id == User.user_id)
            .filter(Tweet.tweet_about == candidate)
            .group_by(User.user_id, User.user_name, User.user_screen_name)
            .order_by(sort_order("total_engagement"))
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_popular_tweets_by_users(user_ids, sort_order, limit=10, by="total_engagement"):
        engagement = Tweet.likes + Tweet.retweet_count
        sort_by = {
            "total_engagement": engagement,
            "likes": Tweet.likes,
            "retweets": Tweet.retweet_count
        }.get(by)
        return (
            db.session.query(
                Tweet.tweet_id,
                Tweet.tweet,
                Tweet.likes,
                Tweet.retweet_count,
                Tweet.source,
                Tweet.created_at,
                User.user_name,
                User.user_screen_name
            )
            .join(User, Tweet.user_id == User.user_id)
            .filter(Tweet.user_id.in_(user_ids))
            .order_by(sort_order(sort_by))
            .limit(limit)
            .all()
        )
    
    @staticmethod
    def get_influential_users(candidate, limit):
        sql = text(f"""
            SELECT 
                u.user_id, 
                u.user_name, 
                u.user_followers_count,
                ROUND(SUM(t.likes + t.retweet_count) / NULLIF(u.user_followers_count, 0), 2) AS engagement_ratio
            FROM users u
            JOIN tweets t ON u.user_id = t.user_id
            WHERE t.tweet_about = :candidate
            GROUP BY u.user_id, u.user_name, u.user_followers_count
            HAVING ROUND(SUM(t.likes + t.retweet_count) / NULLIF(u.user_followers_count, 0), 2) IS NOT NULL
            ORDER BY engagement_ratio DESC
            LIMIT :limit;
        """)
        with current_app.app_context():
            result = db.session.execute(sql, {"candidate": candidate, "limit": limit})
            return result.fetchall(), result.keys()
