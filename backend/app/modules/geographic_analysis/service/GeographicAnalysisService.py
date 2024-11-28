from app.modules.geographic_analysis.repository.GeographicAnalysisRepository import GeographicAnalysisRepository

class GeographicAnalysisService:
    @staticmethod
    def get_most_tweets_by_country(limit=10, sort_by="tweet_count", order="DESC"):
        rows, keys = GeographicAnalysisRepository.get_most_tweets_by_country(limit, sort_by, order)
        return [dict(zip(keys, row)) for row in rows]

    @staticmethod
    def get_city_level_analysis(limit=10, sort_by="tweet_count", order="DESC"):
        rows, keys = GeographicAnalysisRepository.get_city_level_analysis(limit, sort_by, order)
        return [dict(zip(keys, row)) for row in rows]

    @staticmethod
    def get_top_tweets_by_region(filters, sort_by="likes", order="DESC", limit=10):
        rows, keys = GeographicAnalysisRepository.get_top_tweets_by_region(filters, sort_by, order, limit)
        return [dict(zip(keys, row)) for row in rows]