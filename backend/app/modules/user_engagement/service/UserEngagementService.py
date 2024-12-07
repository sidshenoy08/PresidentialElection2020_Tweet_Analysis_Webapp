from app.modules.user_engagement.repository.UserEngagementRepository import UserEngagementRepository
from sqlalchemy import desc, asc

class UserEngagementService:
    @staticmethod
    def get_top_users_by_engagement(order="desc", limit=10):
        sort_order = desc if order == "desc" else asc
        users = UserEngagementRepository.get_top_users_by_engagement(sort_order, limit)
        return [row._asdict() for row in users]

    @staticmethod
    def get_user_activity_breakdown(candidate, order="desc", limit=10):
        sort_order = desc if order == "desc" else asc
        users = UserEngagementRepository.get_user_activity_breakdown(candidate, sort_order, limit)
        return [row._asdict() for row in users]

    @staticmethod
    def get_popular_tweets_by_users(user_ids, order="desc", by="total_engagement"):
        sort_order = desc if order == "desc" else asc
        tweets = UserEngagementRepository.get_popular_tweets_by_users(user_ids, sort_order, by)
        return [row._asdict() for row in tweets]
    
    @staticmethod
    def get_influential_users(candidate="Trump", limit=10):
        rows, keys = UserEngagementRepository.get_influential_users(candidate, limit)
        return [dict(zip(keys, row)) for row in rows]