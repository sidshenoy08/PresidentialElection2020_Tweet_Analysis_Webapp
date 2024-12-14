# import unittest
# from unittest.mock import patch
# from datetime import datetime
# from app.modules.homepage.service.HomepageService import HomepageService

# class TestHomepageService(unittest.TestCase):

#     @patch('app.modules.homepage.service.HomepageService.HomepageRepository.get_total_tweets_overview')
#     def test_get_total_tweets_overview(self, mock_get_total_tweets_overview):
#         mock_get_total_tweets_overview.return_value = {'total_tweets': 1000, 'unique_users': 500}
        
#         result = HomepageService.get_total_tweets_overview('2020-01-01', '2020-12-31')
#         expected = {'total_tweets': 1000, 'unique_users': 500}
#         self.assertEqual(result, expected)
#         mock_get_total_tweets_overview.assert_called_once_with(datetime(2020, 1, 1), datetime(2020, 12, 31))

#     @patch('app.modules.homepage.service.HomepageService.HomepageRepository.get_total_tweets_overview')
#     def test_get_total_tweets_overview_no_dates(self, mock_get_total_tweets_overview):
#         mock_get_total_tweets_overview.return_value = {'total_tweets': 1000, 'unique_users': 500}
        
#         result = HomepageService.get_total_tweets_overview()
#         expected = {'total_tweets': 1000, 'unique_users': 500}
#         # self.assertEqual(result, expected)
#         self.assertThrows(ValueError, HomepageService.get_total_tweets_overview)    
#         mock_get_total_tweets_overview.assert_called_once_with(None, None)

#     @patch('app.modules.homepage.service.HomepageService.HomepageRepository.get_total_tweets_overview')
#     def test_get_total_tweets_overview_invalid_date_format(self):
#         with self.assertRaises(ValueError) as context:
#             HomepageService.get_total_tweets_overview('invalid-date', '2020-12-31')
#         self.assertEqual(str(context.exception), "Invalid date format. Use YYYY-MM-DD format")

#     @patch('app.modules.homepage.service.HomepageService.HomepageRepository.get_total_tweets_overview')
#     def test_get_total_tweets_overview_start_date_after_end_date(self):
#         with self.assertRaises(ValueError) as context:
#             HomepageService.get_total_tweets_overview('2020-12-31', '2020-01-01')
#         self.assertEqual(str(context.exception), "Start date cannot be after end date")

#     # @patch('app.modules.homepage.service.HomepageService.HomepageRepository.get_trending_candidates')
#     # def test_get_trending_candidates(self, mock_get_trending_candidates):
#     #     mock_get_trending_candidates.return_value = [{'candidate': 'Trump', 'tweet_count': 1000}]
#     #     result = HomepageService.get_trending_candidates(5, 'tweet_count', 'desc')
#     #     expected = [{'candidate': 'Trump', 'tweet_count': 1000}]
#     #     self.assertEqual(result, expected)
#     #     mock_get_trending_candidates.assert_called_once_with(5, 'tweet_count', 'desc')

#     @patch('app.modules.homepage.service.HomepageService.HomepageRepository.get_most_active_users')
#     def test_get_most_active_users(self, mock_get_most_active_users):
#         mock_get_most_active_users.return_value = [{'user_name': 'user1', 'tweet_count': 1000}]
        
#         result = HomepageService.get_most_active_users(5, 1, 'tweet_count', 'desc')
#         expected = [{'user_name': 'user1', 'tweet_count': 1000}]
#         self.assertEqual(result, expected)
#         mock_get_most_active_users.assert_called_once_with(5, 0, 'tweet_count', 'desc')
    
#     @patch('app.modules.homepage.service.HomepageService.HomepageRepository.get_tweet_stats_by_candidate')
#     def test_get_tweet_stats_by_candidate(self, mock_get_tweet_stats_by_candidate):
#         mock_get_tweet_stats_by_candidate.return_value = {'candidate': 'Trump', 'tweet_count': 1000}
#         result = HomepageService.get_tweet_stats_by_candidate()
#         expected = [{'candidate': 'Trump', 'tweet_count': 1000}]
#         self.assertEqual(result, expected)
#         mock_get_tweet_stats_by_candidate.assert_called_once()

# if __name__ == '__main__':
#     unittest.main()