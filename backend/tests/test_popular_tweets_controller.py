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

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_top_tweets_by_likes')
def test_get_top_tweets_by_likes(mock_get_top_tweets_by_likes, client):
    mock_data = [
        {
        "city": "Washington",
        "likes": 25987,
        "retweet_count": 5986,
        "state": "District of Columbia",
        "tweet": "The White House still has not released a health care plan. #60Minutes #Trump https://t.co/hvz3VUE1J2",
        "tweet_id": 1320517598568734720,
        "user_name": "Paula Reid"
    }
    ]
    mock_get_top_tweets_by_likes.return_value = mock_data
    response = client.get('/api/popular-tweets/likes')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_top_tweets_by_likes')
def test_get_top_tweets_by_likes_with_params(mock_get_top_tweets_by_likes, client):
    mock_data = [
        {
        "city": "Washington",
        "likes": 25987,
        "retweet_count": 5986,
        "state": "District of Columbia",
        "tweet": "The White House still has not released a health care plan. #60Minutes #Trump https://t.co/hvz3VUE1J2",
        "tweet_id": 1320517598568734720,
        "user_name": "Paula Reid"
    }
    ]
    mock_get_top_tweets_by_likes.return_value = mock_data
    response = client.get('/api/popular-tweets/likes?limit=4&order=desc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_top_tweets_by_likes.assert_called_with("desc", 4)

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_top_tweets_by_retweets')
def test_get_top_tweets_by_retweets(mock_get_top_tweets_by_retweets, client):
    mock_data = [
        {
        "city": "Washington",
        "likes": 25987,
        "retweet_count": 5986,
        "state": "District of Columbia",
        "tweet": "The White House still has not released a health care plan. #60Minutes #Trump https://t.co/hvz3VUE1J2",
        "tweet_id": 1320517598568734720,
        "user_name": "Paula Reid"
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
        "city": "Washington",
        "likes": 25987,
        "retweet_count": 5986,
        "state": "District of Columbia",
        "tweet": "The White House still has not released a health care plan. #60Minutes #Trump https://t.co/hvz3VUE1J2",
        "tweet_id": 1320517598568734720,
        "user_name": "Paula Reid"
    }
    ]
    mock_get_top_tweets_by_retweets.return_value = mock_data
    response = client.get('/api/popular-tweets/retweets?limit=4&order=desc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_top_tweets_by_retweets.assert_called_with("desc", 4)

@patch('app.modules.popular_tweets.controller.PopularTweetsController.PopularTweetsService.get_tweet_location_insights')
def test_get_tweet_location_insights(mock_get_tweet_location_insights, client):
    mock_data = [
        {
        "city": "Washington",
        "likes": 25987,
        "retweet_count": 5986,
        "state": "District of Columbia",
        "tweet": "The White House still has not released a health care plan. #60Minutes #Trump https://t.co/hvz3VUE1J2",
        "tweet_id": 1320517598568734720,
        "user_name": "Paula Reid"
    }
    ]
    mock_get_tweet_location_insights.return_value = mock_data
    response = client.get('/api/popular-tweets/location-insights')
    assert response.status_code == 200
    assert response.json == mock_data