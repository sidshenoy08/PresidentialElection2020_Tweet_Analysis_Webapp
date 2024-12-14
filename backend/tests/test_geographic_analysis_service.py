import unittest
from unittest.mock import patch
from app.modules.geographic_analysis.service.GeographicAnalysisService import GeographicAnalysisService

class TestGeographicAnalysisService(unittest.TestCase):
    @patch('app.modules.geographic_analysis.service.GeographicAnalysisService.GeographicAnalysisRepository.get_most_tweets_by_country')
    def test_get_most_tweets_by_country(self, mock_get_most_tweets_by_country):
        mock_get_most_tweets_by_country.return_value = ([(100, 'USA')], ['tweet_count', 'country'])
        result = GeographicAnalysisService.get_most_tweets_by_country()
        expected = [{'tweet_count': 100, 'country': 'USA'}]
        self.assertEqual(result, expected)

    @patch('app.modules.geographic_analysis.service.GeographicAnalysisService.GeographicAnalysisRepository.get_city_level_analysis')
    def test_get_city_level_analysis(self, mock_get_city_level_analysis):
        mock_get_city_level_analysis.return_value = ([(50, 'New York')], ['tweet_count', 'city'])
        result = GeographicAnalysisService.get_city_level_analysis()
        expected = [{'tweet_count': 50, 'city': 'New York'}]
        self.assertEqual(result, expected)

    @patch('app.modules.geographic_analysis.service.GeographicAnalysisService.GeographicAnalysisRepository.get_top_tweets_by_region')
    def test_get_top_tweets_by_region(self, mock_get_top_tweets_by_region):
        mock_get_top_tweets_by_region.return_value = ([(200, 'California')], ['likes', 'region'])
        filters = {'country': 'USA'}
        result = GeographicAnalysisService.get_top_tweets_by_region(filters)
        expected = [{'likes': 200, 'region': 'California'}]
        self.assertEqual(result, expected)
    
    @patch('app.modules.geographic_analysis.service.GeographicAnalysisService.GeographicAnalysisRepository.get_engagement_by_timezone')
    def test_get_engagement_by_timezone(self, mock_get_engagement_by_timezone):
        mock_get_engagement_by_timezone.return_value = ([(45, 50, 25, 40, 30)], ['lat', 'long', 'tweet_count', 'likes', 'retweets'])
        result = GeographicAnalysisService.get_engagement_by_timezone()
        expected = [{'time_zone': 'Asia/Aqtau', 'tweet_count': 25, 'likes': 40, 'retweets': 30}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()