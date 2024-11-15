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
    def get_most_active_users(limit=5):
        res = HomepageRepository.get_most_active_users(limit)
        return [row._asdict() for row in res]