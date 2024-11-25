from app.modules.engagement_trends.repository.EngagementTrendsRepository import EngagementTrendsRepository
import pandas as pd

class EngagementTrendsService:

    @staticmethod
    def get_engagement_spike_days(candidate, threshold=1.5, sort_by="date", order="asc"):
        # Validating input
        if threshold <= 0:
            raise ValueError("Threshold must be a positive number")
        
        if sort_by not in {"date", "engagement"}:
            raise ValueError(f"Invalid sort_by value: {sort_by}. Allowed parameters: 'date', 'engagement'")
        spikes = EngagementTrendsRepository.get_engagement_spike_days(candidate, threshold, sort_by, order)

        return [row._asdict() for row in spikes]

    @staticmethod
    def get_rolling_average_comparison(candidate, window=7, sort_by="date", order="asc"):
        #Validating input
        window = int(window)
        if window <= 0:
            raise ValueError("Window must be a positive number")
        
        if sort_by not in {"date", "engagement", "rolling_avg"}:
            raise ValueError(f"Invalid sort_by value: {sort_by}. Allowed parameters: 'date', 'engagement', 'rolling_avg'")

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
    def get_high_volume_days(candidate, limit=5, page=1, sort_by="engagement", order="desc"):
        #Validating input
        page = int(page)
        limit = int(limit)
        if limit <= 0:
            raise ValueError("Limit must be a positive number")
        if page <= 0:
            raise ValueError("Page must be a positive number")
        if sort_by not in {"date", "engagement"}:
            raise ValueError(f"Invalid sort_by value: {sort_by}. Allowed parameters: 'date', 'engagement'")
        offset = (page - 1) * limit
        days = EngagementTrendsRepository.get_high_volume_days(candidate, limit+offset, sort_by, order)
        return [row._asdict() for row in days]
