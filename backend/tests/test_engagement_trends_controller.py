import pytest
from flask import Flask, jsonify, request
from unittest.mock import patch
from app import create_app
from app.modules.engagement_trends.controller.EngagementTrendsController import EngagementTrendsController

# Tests for File: tweet-analysis-app/backend/app/modules/engagement_trends/controller/test_EngagementTrendsController.py

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

@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_engagement_spike_days')
def test_get_engagement_spike_days(mock_get_engagement_spike_days, client):
    mock_data = [
        {
            "date": "Thu, 15 Oct 2020 00:00:00 GMT",
            "engagement": 150000
        }
    ]
    mock_get_engagement_spike_days.return_value = mock_data
    response = client.get('/api/engagement-trends/spikes')
    assert response.status_code == 200
    assert response.json == mock_data


@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_rolling_average_comparison')
def test_get_rolling_average_comparison(mock_get_rolling_average_comparison, client):
    mock_data = [
        {
            "date": "Sun, 08 Nov 2020 00:00:00 GMT",
        "engagement": 124056,
        "rolling_avg": 196056.57142857142
        }
    ]
    mock_get_rolling_average_comparison.return_value = mock_data

    response = client.get('/api/engagement-trends/rolling-average')
    
    assert response.status_code == 200
    assert response.json == mock_data
    # mock_get_rolling_average_comparison.assert_called_with("Trump")


@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_engagement_spike_days')
def test_get_engagement_spike_days_with_params(mock_get_engagement_spike_days, client):
    mock_data = [
        {
            "date": "Thu, 15 Oct 2020 00:00:00 GMT",
            "engagement": 150000
        }
    ]
    mock_get_engagement_spike_days.return_value = mock_data
    response = client.get('/api/engagement-trends/spikes?candidate=Biden&threshold=1.0&sort_by=engagement&order=asc')
    assert response.status_code == 200
    assert response.json == mock_data


@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_engagement_spike_days')
def test_get_engagement_spike_days_with_invalid_params(mock_get_engagement_spike_days, client):
    mock_data = [
        {
            "date": "Thu, 15 Oct 2020 00:00:00 GMT",
            "engagement": 150000
        }
    ]
    mock_get_engagement_spike_days.return_value = mock_data
    response = client.get('/api/engagement-trends/spikes?candidate=Ronaldo&threshold=-1.0&sort_by=xyz&order=DX')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_rolling_average_comparison')
def test_get_rolling_average_comparison_with_params(mock_get_rolling_average_comparison, client):
    mock_data = [
        {
            "date": "Sun, 08 Nov 2020 00:00:00 GMT",
        "engagement": 124056,
        "rolling_avg": 196056.57142857142
        }
    ]
    mock_get_rolling_average_comparison.return_value = mock_data

    response = client.get('/api/engagement-trends/rolling-average?candidate=Biden&window=14&sort_by=engagement&order=asc')
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_rolling_average_comparison.assert_called_with("Biden", 14, "engagement", "asc")

@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_rolling_average_comparison')
def test_get_rolling_average_comparison_with_invalid_params(mock_get_rolling_average_comparison, client):
    mock_data = [
        {
            "date": "Sun, 08 Nov 2020 00:00:00 GMT",
        "engagement": 124056,
        "rolling_avg": 196056.57142857142
        }
    ]
    mock_get_rolling_average_comparison.return_value = mock_data

    response = client.get('/api/engagement-trends/rolling-average?candidate=XYZ&window=-1&sort_by=random&order=random')
    
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_rolling_average_comparison.assert_called_with("Biden", 14, "engagement", "asc")


@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_high_volume_days')
def test_get_high_volume_days(mock_get_high_volume_days, client):
    mock_data = [
        {
        "candidate": "Biden",
        "total_engagement": 611806,
        "tweet_count": 31170,
        "tweet_date": "Sat, 07 Nov 2020 00:00:00 GMT"
    }
    ]
    mock_get_high_volume_days.return_value = mock_data
    response = client.get('/api/engagement-trends/high-volume-days')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.engagement_trends.controller.EngagementTrendsController.EngagementTrendsService.get_weekly_sentiment_analysis')
def test_get_weekly_sentiment_analysis(mock_get_weekly_sentiment_analysis, client):
    mock_data = [
        {
        "negative": 6254,
        "neutral": 5808,
        "positive": 5465,
        "tweet_count": 17527,
        "week_start": "Mon, 12 Oct 2020 00:00:00 GMT"
    }
    ]
    mock_get_weekly_sentiment_analysis.return_value = mock_data
    response = client.get('/api/engagement-trends/weekly-sentiment')
    assert response.status_code == 200
    assert response.json == mock_data