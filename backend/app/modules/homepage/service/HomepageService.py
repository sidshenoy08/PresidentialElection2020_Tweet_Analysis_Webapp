from app.modules.homepage.repository.HomepageRepository import HomepageRepository
from datetime import datetime

class HomepageService:

    @staticmethod
    def get_total_tweets_overview(start_date_str=None, end_date_str=None):
        try:
            if start_date_str:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            if end_date_str:
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD format")
        
        if start_date and end_date and start_date > end_date:
            raise ValueError("Start date cannot be after end date")
        return HomepageRepository.get_total_tweets_overview(start_date, end_date)

    @staticmethod
    def get_trending_candidates(limit=5, sort_by="tweet_count", order="desc"): 
        res = HomepageRepository.get_trending_candidates(limit, sort_by, order)
        return [row._asdict() for row in res]

    @staticmethod
    def get_most_active_users(limit=5, page=1, sort_by="tweet_count", order="desc"):
        offset = (page-1)*limit
        valid_sort_columns = {"tweet_count": "tweet_count", "user_name": "user_name"}
        valid_sort_orders = {"asc": "ASC", "desc": "DESC"}
        if sort_by not in valid_sort_columns:
            raise ValueError(f"Invalid sort column. Valid columns are {valid_sort_columns.keys()}")
        if order not in valid_sort_orders:
            raise ValueError(f"Invalid order. Valid orders are {valid_sort_orders.keys()}")
        rows, columns = HomepageRepository.get_most_active_users(limit, offset, sort_by, order)
        return [dict(zip(columns, row)) for row in rows]
    
    @staticmethod
    def get_tweet_stats_by_candidate():
        rows, columns = HomepageRepository.get_tweet_stats_by_candidate()
        return [dict(zip(columns, row)) for row in rows]
