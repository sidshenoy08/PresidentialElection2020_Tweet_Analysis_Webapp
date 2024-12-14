import unittest
from unittest.mock import patch
from app.modules.optimization.service.OptimizationService import OptimizationService

class TestOptimizationService(unittest.TestCase):

    @patch('app.modules.optimization.service.OptimizationService.OptimizationRepository.get_most_tweeted_about_by_user')
    def test_get_most_tweeted_about_by_user(self, mock_get_most_tweeted_about_by_user):
        mock_get_most_tweeted_about_by_user.return_value = ([(1, 'user1')], ['tweet_count', 'user'])
        
        result = OptimizationService.get_most_tweeted_about_by_user()
        expected = [{'tweet_count': 1, 'user': 'user1'}]
        self.assertEqual(result, expected)

    @patch('app.modules.optimization.service.OptimizationService.OptimizationRepository.get_weekly_engagement_with_events')
    def test_get_weekly_engagement_with_events(self, mock_get_weekly_engagement_with_events):
        mock_get_weekly_engagement_with_events.return_value = ([(100, '2020-11-03')], ['engagement_count', 'date'])
        event_dates = ['2020-11-03']
        
        result = OptimizationService.get_weekly_engagement_with_events(event_dates)
        expected = [{'engagement_count': 100, 'date': '2020-11-03'}]
        self.assertEqual(result, expected)

    @patch('app.modules.optimization.service.OptimizationService.OptimizationRepository.get_user_engagement_with_candidate')
    def test_get_user_engagement_with_candidate(self, mock_get_user_engagement_with_candidate):
        mock_get_user_engagement_with_candidate.return_value = ([(200, 'candidate1')], ['engagement_count', 'candidate'])
        
        result = OptimizationService.get_user_engagement_with_candidate()
        expected = [{'engagement_count': 200, 'candidate': 'candidate1'}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()