from app.db import db
from app.models import Tweet, User
from sqlalchemy import func, desc, asc, case

class UserEngagementRepository:
    @staticmethod
    def get_top_users_by_engagement(sort_order, limit=10):
        return (
            db.session.query(
                User.user_id,
                User.user_name,
                User.user_screen_name,
                func.sum(Tweet.likes + Tweet.retweet_count).label("total_engagement"),
                case(
                    (User.user_followers_count > 0, 
                     func.sum(Tweet.likes + Tweet.retweet_count) / func.max(User.user_followers_count)),
                    else_=0
                ).label("follower_to_engagement_ratio"),
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
    def get_popular_tweets_by_users(user_ids, sort_order, limit=10):
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
            .order_by(sort_order(Tweet.likes + Tweet.retweet_count))
            .limit(limit)
            .all()
        )
