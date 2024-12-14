import pytest
from flask import Flask, jsonify, request
from unittest.mock import patch
from app import create_app
from app.modules.popular_tweets.controller.PopularTweetsController import PopularTweetsController

# Tests for File: tweet-analysis-app/backend/app/modules/popular_tweets/controller/test_PopularTweetsController.py

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_most_popular_tweets')
def test_get_most_popular_tweets(mock_get_most_popular_tweets, client):
    mock_data = [
        {
        "candidate": "Trump",
        "tweet_count": 100
    }
    ]
    mock_get_most_popular_tweets.return_value = mock_data
    response = client.get('/api/popular-tweets/most-popular')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_most_popular_tweets')
def test_get_most_popular_tweets_with_params(mock_get_most_popular_tweets, client):
    mock_data = [
        {
        "candidate": "Trump",
        "tweet_count": 100
    }
    ]
    mock_get_most_popular_tweets.return_value = mock_data
    response = client.get('/api/popular-tweets/most-popular?limit=4&order=desc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_most_popular_tweets.assert_called_with("desc", 4)

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_top_tweets_by_likes')
def test_get_top_tweets_by_likes(mock_get_top_tweets_by_likes, client):
    mock_data = [
        {
        "candidate": "Trump",
        "tweet_count": 100
    }
    ]
    mock_get_top_tweets_by_likes.return_value = mock_data
    response = client.get('/api/popular-tweets/top-tweets-by-likes')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_top_tweets_by_likes')
def test_get_top_tweets_by_likes_with_params(mock_get_top_tweets_by_likes, client):
    mock_data = [
        {
        "candidate": "Trump",
        "tweet_count": 100
    }
    ]
    mock_get_top_tweets_by_likes.return_value = mock_data
    response = client.get('/api/popular-tweets/top-tweets-by-likes?limit=4&order=desc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_top_tweets_by_likes.assert_called_with("desc", 4)

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_top_tweets_by_retweets')
def test_get_top_tweets_by_retweets(mock_get_top_tweets_by_retweets, client):
    mock_data = [
        {
        "candidate": "Trump",
        "tweet_count": 100
    }
    ]
    mock_get_top_tweets_by_retweets.return_value = mock_data
    response = client.get('/api/popular-tweets/top-tweets-by-retweets')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_top_tweets_by_retweets')
def test_get_top_tweets_by_retweets_with_params(mock_get_top_tweets_by_retweets, client):
    mock_data = [
        {
        "candidate": "Trump",
        "tweet_count": 100
    }
    ]
    mock_get_top_tweets_by_retweets.return_value = mock_data
    response = client.get('/api/popular-tweets/top-tweets-by-retweets?limit=4&order=desc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_top_tweets_by_retweets.assert_called_with("desc", 4)