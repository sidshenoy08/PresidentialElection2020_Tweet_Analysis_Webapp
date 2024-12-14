import pytest
from flask import Flask, jsonify, request
from unittest.mock import patch
from app import create_app
from app.modules.homepage.controller.HomepageController import HomepageController

# Tests for File: tweet-analysis-app/backend/app/modules/homepage/controller/test_homepage_controller.py

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

@patch('app.modules.homepage.controller.HomepageController.HomepageService.get_total_tweets_overview')
def test_get_total_tweets_overview(mock_get_total_tweets_overview, client):
    mock_data = {
        "total_tweets": 100,
        "total_retweets": 50,
        "total_replies": 25,
        "total_quotes": 25
    }
    mock_get_total_tweets_overview.return_value = mock_data
    response = client.get('/api/homepage/overview')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.homepage.controller.HomepageController.HomepageService.get_trending_candidates')
def test_get_trending_candidates(mock_get_trending_candidates, client):
    mock_data = [
        {
        "candidate": "Trump",
        "tweet_count": 100
    }
    ]
    mock_get_trending_candidates.return_value = mock_data
    response = client.get('/api/homepage/trending-candidates')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.homepage.controller.HomepageController.HomepageService.get_most_active_users')
def test_get_most_active_users(mock_get_most_active_users, client):
    mock_data = [
        {
        "user_id": 139823781,
        "user_name": "bettemidler",
        "user_screen_name": "BetteMidler",
        "tweet_count": 100
    }
    ]
    mock_get_most_active_users.return_value = mock_data
    response = client.get('/api/homepage/most-active-users')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.homepage.controller.HomepageController.HomepageService.get_tweet_stats_by_candidate')
def test_get_tweet_stats_by_candidate(mock_get_tweet_stats_by_candidate, client):
    mock_data = {
        "total_tweets": 100,
        "total_retweets": 50,
        "total_replies": 25,
        "total_quotes": 25
    }
    mock_get_tweet_stats_by_candidate.return_value = mock_data
    response = client.get('/api/homepage/tweet-stats-by-candidate')
    assert response.status_code == 200
    assert response.json == mock_data