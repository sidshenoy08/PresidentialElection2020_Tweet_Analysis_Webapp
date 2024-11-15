from app.modules.homepage.repository.homepageRepo import HomepageRepository

class HomepageService:

    @staticmethod
    def get_total_tweets_overview():
        return HomepageRepository.get_total_tweets_overview()

    @staticmethod
    def get_trending_candidates(limit=5): #TODO change laater to pageSize
        return HomepageRepository.get_trending_candidates(limit)

    @staticmethod
    def get_most_active_users(limit=5):
        return HomepageRepository.get_most_active_users(limit)
