import pytest
from flask import Flask, jsonify, request
from unittest.mock import patch
from app import create_app
from app.modules.user_engagement.controller.UserEngagementController import UserEngagementController

# Tests for File: tweet-analysis-app/backend/app/modules/user_engagement/controller/test_UserEngagementController.py

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

@patch('app.modules.user_engagement.controller.UserEngagementController.UserEngagementService.get_top_users_by_engagement')
def test_get_top_users_by_engagement(mock_get_top_users_by_engagement, client):
    mock_data = [
        {
        "engagement_to_followers_ratio": "0.33369765360980263109",
        "followers": 2028435,
        "total_engagement": 676884,
        "user_id": 139823781,
        "user_name": "bettemidler",
        "user_screen_name": "BetteMidler"
    }
    ]
    mock_get_top_users_by_engagement.return_value = mock_data
    response = client.get('/api/user-engagement/top-users')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.user_engagement.controller.UserEngagementController.UserEngagementService.get_top_users_by_engagement')
def test_get_top_users_by_engagement_with_params(mock_get_top_users_by_engagement, client):
    mock_data = [
        {
        "engagement_to_followers_ratio": "0.33369765360980263109",
        "followers": 2028435,
        "total_engagement": 676884,
        "user_id": 139823781,
        "user_name": "bettemidler",
        "user_screen_name": "BetteMidler"
    }
    ]
    response = client.get('/api/user-engagement/top-users?limit=4&order=desc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_top_users_by_engagement.assert_called_with(4, "desc")

@patch('app.modules.user_engagement.controller.UserEngagementController.UserEngagementService.get_top_users_by_engagement')
def test_get_top_users_by_engagement_with_invalid_params(mock_get_top_users_by_engagement, client):
    mock_data = [
        {
        "engagement_to_followers_ratio": "0.33369765360980263109",
        "followers": 2028435,
        "total_engagement": 676884,
        "user_id": 139823781,
        "user_name": "bettemidler",
        "user_screen_name": "BetteMidler"
    }
    ]
    response = client.get('/api/user-engagement/top-users?limit=-4&order=Random')
    assert response.status_code == 200
    assert response.json == mock_data
    # mock_get_user_engagement.assert_called_with("Trump", 1.5, "date", "desc")


@patch('app.modules.user_engagement.controller.UserEngagementController.UserEngagementService.get_user_activity_breakdown')
def test_get_user_activity_breakdown(mock_get_user_activity_breakdown, client):
    mock_data = [
        {
        "total_engagement": 175808,
        "tweet_count": 19,
        "user_id": 139823781,
        "user_name": "bettemidler",
        "user_screen_name": "BetteMidler"
    }
    ]
    mock_get_user_activity_breakdown.return_value = mock_data
    response = client.get('/api/user-engagement/activity-breakdown')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.user_engagement.controller.UserEngagementController.UserEngagementService.get_user_activity_breakdown')
def test_get_user_activity_breakdown_with_params(mock_get_user_activity_breakdown, client):
    mock_data = [
        {
        "total_engagement": 175808,
        "tweet_count": 19,
        "user_id": 139823781,
        "user_name": "bettemidler",
        "user_screen_name": "BetteMidler"
    }
    ]
    response = client.get('/api/user-engagement/activity-breakdown?candidate=Biden&limit=4&order=desc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_user_activity_breakdown.assert_called_with("Biden", 4, "desc")


@patch('app.modules.user_engagement.controller.UserEngagementController.UserEngagementService.get_popular_tweets_by_users')
def test_get_popular_tweets_by_users(mock_get_popular_tweets_by_users, client):
    mock_data = [
        {
        "created_at": "Sun, 08 Nov 2020 16:43:17 GMT",
        "likes": 659,
        "retweet_count": 1579,
        "source": "Twitter for iPhone",
        "tweet": "จะ20Mแล้ว รีไป #มันจบแล้วชนชั้นนํา #ราชภักดิ์ #ประชาสาส์น #ราษฎรสาส์น #Biden2020 #DonaldTrump #AmericaDecides2020 #ชายสั่งมา #whatishappeninginthailand #ม็อบ8พฤศจิกา #มือลั่นเหมือนพ่อมึงเลย  https://t.co/fQFqrsF1Rj",
        "tweet_id": 1325479012093751296,
        "user_name": "แมลงสาปจะฉาบแก",
        "user_screen_name": "pp230901"
    }
    ]
    mock_get_popular_tweets_by_users.return_value = mock_data
    response = client.post('/api/user-engagement/popular-tweets', json={
    "user_ids":["1294010038906888192","1314656874608943104"],
    "order":"desc",
    "by":"total_engagement"
})
    assert response.status_code == 200
    assert response.json == mock_data