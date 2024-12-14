import unittest
from unittest.mock import patch, MagicMock
from app.modules.popular_tweets.service.PopularTweetsService import PopularTweetsService

class TestPopularTweetsService(unittest.TestCase):

    @patch('app.modules.popular_tweets.service.PopularTweetsService.PopularTweetsRepository.get_top_tweets_by_retweets')
    def test_get_top_tweets_by_retweets(self, mock_get_top_tweets_by_retweets):
        mock_tweet = MagicMock()
        mock_tweet._asdict.return_value = {'id': 1, 'retweets': 100}
        mock_get_top_tweets_by_retweets.return_value = [mock_tweet]
        
        result = PopularTweetsService.get_top_tweets_by_retweets('Trump')
        expected = [{'id': 1, 'retweets': 100}]
        self.assertEqual(result, expected)

    @patch('app.modules.popular_tweets.service.PopularTweetsService.PopularTweetsRepository.get_top_tweets_by_likes')
    def test_get_top_tweets_by_likes(self, mock_get_top_tweets_by_likes):
        mock_tweet = MagicMock()
        mock_tweet._asdict.return_value = {'id': 2, 'likes': 200}
        mock_get_top_tweets_by_likes.return_value = [mock_tweet]
        
        result = PopularTweetsService.get_top_tweets_by_likes('Biden')
        expected = [{'id': 2, 'likes': 200}]
        self.assertEqual(result, expected)

    @patch('app.modules.popular_tweets.service.PopularTweetsService.PopularTweetsRepository.get_tweet_location_insights')
    def test_get_tweet_location_insights(self, mock_get_tweet_location_insights):
        mock_location = MagicMock()
        mock_location._asdict.return_value = {'location': 'USA', 'count': 300}
        mock_get_tweet_location_insights.return_value = [mock_location]
        
        result = PopularTweetsService.get_tweet_location_insights('Trump')
        expected = [{'location': 'USA', 'count': 300}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()