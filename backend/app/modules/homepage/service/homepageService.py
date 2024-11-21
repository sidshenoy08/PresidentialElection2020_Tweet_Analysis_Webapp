from app.modules.homepage.repository.homepageRepo import HomepageRepository

class HomepageService:

    @staticmethod
    def get_total_tweets_overview():
        return HomepageRepository.get_total_tweets_overview()

    @staticmethod
    def get_trending_candidates(limit=5): #TODO change laater to pageSize
        res = HomepageRepository.get_trending_candidates(limit)
        return [row._asdict() for row in res]

    @staticmethod
    def get_most_active_users(limit=5, page=1, sort_by="tweet_count", order="desc"):
        offset = (page-1)*limit
        res = HomepageRepository.get_most_active_users(limit, offset, sort_by, order)
        return [row._asdict() for row in res]
