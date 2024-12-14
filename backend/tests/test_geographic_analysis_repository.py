import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import create_app
from app.modules.geographic_analysis.repository.GeographicAnalysisRepository import GeographicAnalysisRepository

class TestGeographicAnalysisRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a Flask app context for the test
        cls.app = create_app()
        cls.app.config.update({
            "TESTING": True,
        })
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
    
    
    # @patch('app.modules.geographic_analysis.repository.GeographicAnalysisRepository.current_app')

    @patch('app.modules.geographic_analysis.repository.GeographicAnalysisRepository.db.session.execute')
    @patch('app.modules.geographic_analysis.repository.GeographicAnalysisRepository.text')
    def test_get_most_tweets_by_country(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [('USA', 100)]
        mock_result.keys.return_value = ['country', 'tweet_count']
        mock_execute.return_value = mock_result
        
        # with mock_current_app.app_context():
        result, keys = GeographicAnalysisRepository.get_most_tweets_by_country('tweet_count', 'DESC')
        
        expected_result = [('USA', 100)]
        expected_keys = ['country', 'tweet_count']
        
        self.assertEqual(result, expected_result)
        self.assertEqual(keys, expected_keys)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql')

    @patch('app.modules.geographic_analysis.repository.GeographicAnalysisRepository.db.session.execute')
    @patch('app.modules.geographic_analysis.repository.GeographicAnalysisRepository.text')
    def test_get_city_level_analysis(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [('New York', 100, 200, 300)]
        mock_result.keys.return_value = ['city', 'tweet_count', 'likes', 'retweets']
        mock_execute.return_value = mock_result
        
        result, keys = GeographicAnalysisRepository.get_city_level_analysis(5, 'tweet_count', 'DESC')
        
        expected_result = [('New York', 100, 200, 300)]
        expected_keys = ['city', 'tweet_count', 'likes', 'retweets']
        
        self.assertEqual(result, expected_result)
        self.assertEqual(keys, expected_keys)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql', {'limit': 5})

    @patch('app.modules.geographic_analysis.repository.GeographicAnalysisRepository.db.session.execute')
    @patch('app.modules.geographic_analysis.repository.GeographicAnalysisRepository.text')
    def test_get_top_tweets_by_region(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [(1, 'tweet', 100, 200, 'user', 'New York, NY, USA')]
        mock_result.keys.return_value = ['tweet_id', 'tweet', 'likes', 'retweet_count', 'user_name', 'location']
        mock_execute.return_value = mock_result
        
        result, keys = GeographicAnalysisRepository.get_top_tweets_by_region({'continent': 'North America'}, 'likes', 'DESC', 10)
        
        expected_result = [(1, 'tweet', 100, 200, 'user', 'New York, NY, USA')]
        expected_keys = ['tweet_id', 'tweet', 'likes', 'retweet_count', 'user_name', 'location']
        
        self.assertEqual(result, expected_result)
        self.assertEqual(keys, expected_keys)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql', {
            'continent': 'North America',
            'country': None,
            'state': None,
            'city': None,
            'limit': 10
        })

if __name__ == '__main__':
    unittest.main()