from app.modules.optimization.repository.OptimizationRepository import OptimizationRepository

class OptimizationService:

    @staticmethod
    def get_most_tweeted_about_by_user():
        results, keys = OptimizationRepository.get_most_tweeted_about_by_user()
        return [dict(zip(keys, row)) for row in results]
    
    @staticmethod
    def get_weekly_engagement_with_events(event_dates):
        results, keys = OptimizationRepository.get_weekly_engagement_with_events(event_dates)
        return [dict(zip(keys, row)) for row in results]
    
    @staticmethod
    def get_user_engagement_with_candidate():
        results, keys = OptimizationRepository.get_user_engagement_with_candidate()
        return [dict(zip(keys, row)) for row in results]
