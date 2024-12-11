from app.modules.engagement_trends.repository.EngagementTrendsRepository import EngagementTrendsRepository
import pandas as pd

class EngagementTrendsService:

    @staticmethod
    def get_engagement_spike_days(candidate, threshold=1.5, sort_by="date", order="asc"):
        rows, keys = EngagementTrendsRepository.get_engagement_spike_days(candidate, threshold, sort_by, order)
        return [dict(zip(keys, row)) for row in rows]

    @staticmethod
    def get_rolling_average_comparison(candidate, window=7, sort_by="date", order="asc"):
        data = EngagementTrendsRepository.get_daily_engagement(candidate)
        if not data:
            return []
        df = pd.DataFrame(data, columns=["date", "engagement"])
        ord = order == "asc"
        # Calculate rolling average using pandas
        df["rolling_avg"] = df["engagement"].rolling(window=window, min_periods=1).mean()
        df.sort_values(by=sort_by, ascending=ord, inplace=True)
        # Convert to list of dictionaries
        return df.to_dict(orient="records")

    @staticmethod
    def get_high_volume_days(rank_limit, sort_by, order):
        rows, keys = EngagementTrendsRepository.get_high_volume_days(rank_limit, sort_by, order)
        return [dict(zip(keys, row)) for row in rows]
    
    @staticmethod
    def get_weekly_sentiment_analysis(candidate="Trump", start_date=None, end_date=None):
        rows, keys = EngagementTrendsRepository.get_weekly_sentiment_analysis(candidate, start_date, end_date)
        return [dict(zip(keys, row)) for row in rows]