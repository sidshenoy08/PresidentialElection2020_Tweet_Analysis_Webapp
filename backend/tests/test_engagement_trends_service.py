import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from app.modules.engagement_trends.service.EngagementTrendsService import EngagementTrendsService

class TestEngagementTrendsService(unittest.TestCase):

    @patch('app.modules.engagement_trends.service.EngagementTrendsService.EngagementTrendsRepository.get_engagement_spike_days')
    def test_get_engagement_spike_days(self, mock_get_engagement_spike_days):
        mock_get_engagement_spike_days.return_value = ([(1, '2020-11-03')], ['spike_count', 'date'])
        
        result = EngagementTrendsService.get_engagement_spike_days('Trump')
        expected = [{'spike_count': 1, 'date': '2020-11-03'}]
        self.assertEqual(result, expected)

    @patch('app.modules.engagement_trends.service.EngagementTrendsService.EngagementTrendsRepository.get_daily_engagement')
    def test_get_rolling_average_comparison(self, mock_get_daily_engagement):
        mock_get_daily_engagement.return_value = [('2020-11-01', 100), ('2020-11-02', 200), ('2020-11-03', 300)]
        
        result = EngagementTrendsService.get_rolling_average_comparison('Biden', window=2)
        expected = [
            {'date': '2020-11-01', 'engagement': 100, 'rolling_avg': 100.0},
            {'date': '2020-11-02', 'engagement': 200, 'rolling_avg': 150.0},
            {'date': '2020-11-03', 'engagement': 300, 'rolling_avg': 250.0}
        ]
        self.assertEqual(result, expected)

    @patch('app.modules.engagement_trends.service.EngagementTrendsService.EngagementTrendsRepository.get_daily_engagement')
    def test_get_rolling_average_comparison_empty(self, mock_get_daily_engagement):
        mock_get_daily_engagement.return_value = []
        
        result = EngagementTrendsService.get_rolling_average_comparison('Biden', window=2)
        expected = []
        self.assertEqual(result, expected)

    @patch('app.modules.engagement_trends.service.EngagementTrendsService.EngagementTrendsRepository.get_high_volume_days')
    def test_get_high_volume_days(self, mock_get_high_volume_days):
        mock_get_high_volume_days.return_value = ([(1, '2020-11-03')], ['volume', 'date'])
        
        result = EngagementTrendsService.get_high_volume_days(1, 'date', 'asc')
        expected = [{'volume': 1, 'date': '2020-11-03'}]
        self.assertEqual(result, expected)

    @patch('app.modules.engagement_trends.service.EngagementTrendsService.EngagementTrendsRepository.get_weekly_sentiment_analysis')
    def test_get_weekly_sentiment_analysis(self, mock_get_weekly_sentiment_analysis):
        mock_get_weekly_sentiment_analysis.return_value = ([(1, '2020-11-03')], ['sentiment_count', 'date'])
        
        result = EngagementTrendsService.get_weekly_sentiment_analysis('Trump')
        expected = [{'sentiment_count': 1, 'date': '2020-11-03'}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()