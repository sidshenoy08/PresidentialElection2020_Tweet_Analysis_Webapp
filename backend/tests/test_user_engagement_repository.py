import unittest
from unittest.mock import patch, MagicMock
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

    @patch('app.modules.user_engagement.repository.UserEngagementRepository.db.session.query')
    def test_get_top_users_by_engagement(self, mock_query):
        mock_query_instance = MagicMock()
        mock_query.return_value = mock_query_instance
        mock_query_instance.join.return_value = mock_query_instance
        mock_query_instance.group_by.return_value = mock_query_instance
        mock_query_instance.order_by.return_value = mock_query_instance
        mock_query_instance.limit.return_value = mock_query_instance
        mock_query_instance.all.return_value = [
            (1, 'user1', 'user1_screen', 100, 0.1)
        ]
        
        result = UserEngagementRepository.get_top_users_by_engagement('desc', 10)
        
        expected_result = [
            (1, 'user1', 'user1_screen', 100, 0.1)
        ]
        
        self.assertEqual(result, expected_result)
        mock_query.assert_called_once()
        mock_query_instance.join.assert_called_once()
        mock_query_instance.group_by.assert_called_once()
        mock_query_instance.order_by.assert_called_once()
        mock_query_instance.limit.assert_called_once_with(10)
        mock_query_instance.all.assert_called_once()

if __name__ == '__main__':
    unittest.main()