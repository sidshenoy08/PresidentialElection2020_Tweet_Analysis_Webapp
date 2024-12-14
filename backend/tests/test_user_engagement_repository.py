import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import create_app
from sqlalchemy import desc, asc
from app.modules.user_engagement.repository.UserEngagementRepository import UserEngagementRepository

class TestUserEngagementRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a Flask app context for the test
        cls.app = create_app()
        cls.app.config.update({
            "TESTING": True,
        })
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        # Pop the app context after tests
        cls.app_context.pop()

    @patch('app.modules.user_engagement.repository.UserEngagementRepository.db.session.query')
    def test_get_top_users_by_engagement(self, mock_query):
        # Mock query
        mock_query_instance = MagicMock()
        mock_query.return_value = mock_query_instance
        mock_query_instance.join.return_value = mock_query_instance
        mock_query_instance.group_by.return_value = mock_query_instance
        mock_query_instance.order_by.return_value = mock_query_instance
        mock_query_instance.limit.return_value = mock_query_instance
        mock_query_instance.all.return_value = [
            {
                "user_id": "123",
                "user_name": "John Doe",
                "user_screen_name": "johndoe",
                "total_engagement": 1000,
                "engagement_to_followers_ratio": 0.1,
                "followers": 10000
            }
        ]

        # Call the repository function
        result = UserEngagementRepository.get_top_users_by_engagement(desc, 5)

        # Assertions
        expected = [
            {
                "user_id": "123",
                "user_name": "John Doe",
                "user_screen_name": "johndoe",
                "total_engagement": 1000,
                "engagement_to_followers_ratio": 0.1,
                "followers": 10000
            }
        ]
        self.assertEqual(result, expected)
        mock_query.assert_called_once()

    @patch('app.modules.user_engagement.repository.UserEngagementRepository.db.session.execute')
    @patch('app.modules.user_engagement.repository.UserEngagementRepository.text')
    def test_get_user_activity_breakdown(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [
            (123, 'John Doe', 'johndoe', 5000, 20)
        ]
        mock_result.keys.return_value = ['user_id', 'user_name', 'user_screen_name', 'total_engagement', 'tweet_count']
        mock_execute.return_value = mock_result
        result = UserEngagementRepository.get_user_activity_breakdown('Biden', desc, 10)
        expected = [
            (123, 'John Doe', 'johndoe', 5000, 20)
        ], ['user_id', 'user_name', 'user_screen_name', 'total_engagement', 'tweet_count']

        # Assertions
        self.assertEqual(result, expected)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql', {'candidate': 'Biden', 'limit': 10})

    @patch('app.modules.user_engagement.repository.UserEngagementRepository.db.session.query')
    def test_get_popular_tweets_by_users(self, mock_query):
        mock_query_instance = MagicMock()
        mock_query.return_value = mock_query_instance
        mock_query_instance.join.return_value = mock_query_instance
        mock_query_instance.filter.return_value = mock_query_instance
        mock_query_instance.order_by.return_value = mock_query_instance
        mock_query_instance.all.return_value = [
            {
                "tweet_id": "1",
                "tweet": "This is a test tweet",
                "likes": 100,
                "retweet_count": 50,
                "source": "Twitter Web App",
                "created_at": "2022-01-01",
                "user_name": "John Doe",
                "user_screen_name": "johndoe"
            }
        ]

        # Call the repository function
        result = UserEngagementRepository.get_popular_tweets_by_users(['123'], desc, 'total_engagement')

        # Assertions
        expected = [
            {
                "tweet_id": "1",
                "tweet": "This is a test tweet",
                "likes": 100,
                "retweet_count": 50,
                "source": "Twitter Web App",
                "created_at": "2022-01-01",
                "user_name": "John Doe",
                "user_screen_name": "johndoe"
            }
        ]
        self.assertEqual(result, expected)
        mock_query.assert_called_once()

    @patch('app.modules.user_engagement.repository.UserEngagementRepository.db.session.execute')
    @patch('app.modules.user_engagement.repository.UserEngagementRepository.text')
    def test_get_influential_users(self, mock_text, mock_execute):
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [
            (123, 'John Doe', 10000, 0.5)
        ]
        mock_result.keys.return_value = ['user_id', 'user_name', 'user_followers_count', 'engagement_ratio']
        mock_execute.return_value = mock_result
        result = UserEngagementRepository.get_influential_users('Biden', 10)
        expected = [
            (123, 'John Doe', 10000, 0.5)
        ], ['user_id', 'user_name', 'user_followers_count', 'engagement_ratio']
        self.assertEqual(result, expected)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql', {'candidate': 'Biden', 'limit': 10})


if __name__ == '__main__':
    unittest.main()