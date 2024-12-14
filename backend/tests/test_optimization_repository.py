import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import create_app
from app.modules.optimization.repository.OptimizationRepository import OptimizationRepository

class TestOptimizationRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a Flask app context for the test
        cls.app = create_app()
        cls.app.config.update({
            "TESTING": True,
        })
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @patch('app.modules.optimization.repository.OptimizationRepository.db.session.execute')
    @patch('app.modules.optimization.repository.OptimizationRepository.text')
    def test_get_most_tweeted_about_by_user(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [(1, 100, 200, 300)]
        mock_result.keys.return_value = ['user_id', 'total_trump_tweets', 'total_likes', 'total_retweets']
        mock_execute.return_value = mock_result
        
        result, keys = OptimizationRepository.get_most_tweeted_about_by_user()
        
        expected_result = [(1, 100, 200, 300)]
        expected_keys = ['user_id', 'total_trump_tweets', 'total_likes', 'total_retweets']
        
        self.assertEqual(result, expected_result)
        self.assertEqual(keys, expected_keys)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql')

    
    @patch('app.modules.optimization.repository.OptimizationRepository.db.session.execute')
    @patch('app.modules.optimization.repository.OptimizationRepository.text')
    def test_get_weekly_engagement_with_events(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [(1, 100, 200, 300)]
        mock_result.keys.return_value = ['user_id', 'total_trump_tweets', 'total_likes', 'total_retweets']
        mock_execute.return_value = mock_result
        
        result, keys = OptimizationRepository.get_weekly_engagement_with_events(['2021-01-01', '2021-01-07'])
        
        expected_result = [(1, 100, 200, 300)]
        expected_keys = ['user_id', 'total_trump_tweets', 'total_likes', 'total_retweets']
        
        self.assertEqual(result, expected_result)
        self.assertEqual(keys, expected_keys)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql', {'event_dates': ['2021-01-01', '2021-01-07']})

    
    @patch('app.modules.optimization.repository.OptimizationRepository.db.session.execute')
    @patch('app.modules.optimization.repository.OptimizationRepository.text')
    def test_get_user_engagement_with_candidate(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [(1, 100, 200, 300)]
        mock_result.keys.return_value = ['user_id', 'total_trump_tweets', 'total_likes', 'total_retweets']
        mock_execute.return_value = mock_result
        
        result, keys = OptimizationRepository.get_user_engagement_with_candidate('Trump')
        
        expected_result = [(1, 100, 200, 300)]
        expected_keys = ['user_id', 'total_trump_tweets', 'total_likes', 'total_retweets']
        
        self.assertEqual(result, expected_result)
        self.assertEqual(keys, expected_keys)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql')

        

if __name__ == '__main__':
    unittest.main()