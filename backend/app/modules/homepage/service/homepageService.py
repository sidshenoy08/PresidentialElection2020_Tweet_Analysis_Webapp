from app.modules.homepage.repository.homepageRepo import HomepageRepository
from datetime import datetime

class HomepageService:

    @staticmethod
    def get_total_tweets_overview(start_date_str=None, end_date_str=None):
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d") if start_date_str else None
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d") if end_date_str else None
        return HomepageRepository.get_total_tweets_overview(start_date, end_date)

    @staticmethod
    def get_trending_candidates(limit=5, sort_by="tweet_count", order="desc"): 
        res = HomepageRepository.get_trending_candidates(limit, sort_by, order)
        return [row._asdict() for row in res]

    @staticmethod
    def get_most_active_users(limit=5, page=1, sort_by="tweet_count", order="desc"):
        offset = (page-1)*limit
        res = HomepageRepository.get_most_active_users(limit, offset, sort_by, order)
        return [row._asdict() for row in res]