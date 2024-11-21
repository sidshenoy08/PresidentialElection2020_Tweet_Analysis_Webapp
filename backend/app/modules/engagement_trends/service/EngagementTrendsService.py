from app.modules.engagement_trends.repository.EngagementTrendsRepository import EngagementTrendsRepository
import pandas as pd

class EngagementTrendsService:

    @staticmethod
    def get_engagement_spike_days(candidate, threshold=1.5):
        spikes = EngagementTrendsRepository.get_engagement_spike_days(candidate, threshold)
        return [row._asdict() for row in spikes]

    @staticmethod
    def get_rolling_average_comparison(candidate, window=7):
        data = EngagementTrendsRepository.get_daily_engagement(candidate)
        df = pd.DataFrame(data, columns=["date", "engagement"])

        # Calculate rolling average using pandas
        df["rolling_avg"] = df["engagement"].rolling(window=window, min_periods=1).mean()

        # Convert to list of dictionaries
        return df.to_dict(orient="records")

    @staticmethod
    def get_high_volume_days(candidate, limit=5):
        days = EngagementTrendsRepository.get_high_volume_days(candidate, limit)
        return [row._asdict() for row in days]
