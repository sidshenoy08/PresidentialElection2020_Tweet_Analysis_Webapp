from app.modules.geographic_analysis.repository.GeographicAnalysisRepository import GeographicAnalysisRepository
from timezonefinder import TimezoneFinder

class GeographicAnalysisService:
    @staticmethod
    def get_most_tweets_by_country(sort_by="tweet_count", order="DESC"):
        rows, keys = GeographicAnalysisRepository.get_most_tweets_by_country(sort_by, order)
        return [dict(zip(keys, row)) for row in rows]

    @staticmethod
    def get_city_level_analysis(limit=10, sort_by="tweet_count", order="DESC"):
        rows, keys = GeographicAnalysisRepository.get_city_level_analysis(limit, sort_by, order)
        return [dict(zip(keys, row)) for row in rows]

    @staticmethod
    def get_top_tweets_by_region(filters, sort_by="likes", order="DESC", limit=10):
        rows, keys = GeographicAnalysisRepository.get_top_tweets_by_region(filters, sort_by, order, limit)
        return [dict(zip(keys, row)) for row in rows]
    
    @staticmethod
    def get_engagement_by_timezone(candidate="Trump"):
        rows, keys = GeographicAnalysisRepository.get_engagement_by_timezone(candidate)
        tf = TimezoneFinder()

        enriched_data = []
        for row in rows:
            record = dict(zip(keys, row))
            time_zone = tf.timezone_at(lat=record['lat'], lng=record['long'])
            if time_zone:
                record['time_zone'] = time_zone
                enriched_data.append(record)

        aggregated_data = {}
        for record in enriched_data:
            tz = record['time_zone']
            if tz not in aggregated_data:
                aggregated_data[tz] = {
                    "tweet_count": 0,
                    "likes": 0,
                    "retweets": 0
                }
            aggregated_data[tz]["tweet_count"] += record["tweet_count"]
            aggregated_data[tz]["likes"] += record["likes"]
            aggregated_data[tz]["retweets"] += record["retweets"]

        sorted_data = sorted(aggregated_data.items(), key=lambda x: x[1]["tweet_count"], reverse=True)
        return [
            {"time_zone": tz, **metrics} for tz, metrics in sorted_data
        ]