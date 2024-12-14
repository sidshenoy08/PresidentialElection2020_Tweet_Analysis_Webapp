import pytest
from flask import Flask, jsonify, request
from unittest.mock import patch
from app import create_app
from app.modules.optimization.controller.OptimizationController import OptimizationController

# Tests for File: tweet-analysis-app/backend/app/modules/optimization/controller/test_OptimizationController.py

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

@patch('app.modules.optimization.controller.OptimizationController.OptimizationService.get_most_tweeted_about_by_user')
def test_get_most_tweeted_about_by_user(mock_get_most_tweeted_about_by_user, client):
    mock_data = [
        {
        "most_tweeted_about": "Trump",
        "total_likes": 954,
        "total_retweets": 426,
        "user_followers_count": 1185,
        "user_id": 8436472,
        "user_join_date": "Sun, 26 Aug 2007 05:56:11 GMT",
        "user_name": "snarke"
    }
    ]
    mock_get_most_tweeted_about_by_user.return_value = mock_data
    response = client.get('/api/optimization/most-tweeted-about')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.optimization.controller.OptimizationController.OptimizationService.get_weekly_engagement_with_events')
def test_get_weekly_engagement_with_events(mock_get_weekly_engagement_with_events, client):
    mock_data = [
        {
        "candidate": "Biden",
        "event_date": "Mon, 12 Oct 2020 00:00:00 GMT",
        "event_engagement": 0,
        "event_tweet_count": 0,
        "tweet_week": "Mon, 12 Oct 2020 00:00:00 GMT",
        "weekly_engagement": 403112,
        "weekly_tweet_count": 10948
    }
    ]
    mock_get_weekly_engagement_with_events.return_value = mock_data
    response = client.post('/api/optimization/weekly-engagement-with-events', json={"event_dates": ["2020-01-01"]})
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.optimization.controller.OptimizationController.OptimizationService.get_user_engagement_with_candidate')
def test_get_user_engagement_with_candidate(mock_get_user_engagement_with_candidate, client):
    mock_data = [
        {
        "candidate": "Biden",
        "engagement_to_followers_ratio": "12.33",
        "total_engagement": 37,
        "total_tweets": 23,
        "user_followers_count": 3,
        "user_id": 1319153749785563136,
        "user_name": "AmPats"
    }
    ]
    mock_get_user_engagement_with_candidate.return_value = mock_data
    response = client.get('/api/optimization/user-engagement-with-candidate')
    assert response.status_code == 200
    assert response.json == mock_data
