import pytest
from flask import Flask, jsonify, request
from unittest.mock import patch
from app import create_app
from app.modules.candidate_analysis.controller.CandidateAnalysisController import CandidateAnalysisController

# Tests for File: tweet-analysis-app/backend/app/modules/candidate_analysis/controller/test_CandidateAnalysisController.py


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

@patch('app.modules.candidate_analysis.controller.CandidateAnalysisController.CandidateAnalysisService.get_region_wise_engagement')
def test_get_region_wise_engagement(mock_get_region_wise_engagement, client):
    mock_data = [
        {
            "country": "Afghanistan",
            "engagement_percentage": "59.26",
            "total_engagement": 112,
            "tweet_about": "Biden"
        },
        {
            "country": "Afghanistan",
            "engagement_percentage": "40.74",
            "total_engagement": 77,
            "tweet_about": "Trump"
        }
    ]
    mock_get_region_wise_engagement.return_value = mock_data
    response = client.get('/api/candidate-analysis/region-wise-engagement')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.candidate_analysis.controller.CandidateAnalysisController.CandidateAnalysisService.get_daily_trends')
def test_get_daily_trends_default(mock_get_daily_trends, client):
    mock_data = [
        {
            "rolling_avg": "52784.00",
            "total_engagement": 52784,
            "tweet_count": 4061,
            "tweet_date": "Thu, 15 Oct 2020 00:00:00 GMT"
        }
    ]
    mock_get_daily_trends.return_value = mock_data

    response = client.get('/api/candidate-analysis/daily-trends')
    
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_daily_trends.assert_called_with("Trump")


@patch('app.modules.candidate_analysis.controller.CandidateAnalysisController.CandidateAnalysisService.get_daily_trends')
def test_get_daily_trends_with_candidate(mock_get_daily_trends, client):
    mock_data = [
        {
            "rolling_avg": "44471.00",
            "total_engagement": 44471,
            "tweet_count": 2766,
            "tweet_date": "Thu, 15 Oct 2020 00:00:00 GMT"
        }
    ]
    mock_get_daily_trends.return_value = mock_data

    response = client.get('/api/candidate-analysis/daily-trends?candidate=Biden')
    
    assert response.status_code == 200
    assert response.json == mock_data
    mock_get_daily_trends.assert_called_with("Biden")

@patch('app.modules.candidate_analysis.controller.CandidateAnalysisController.CandidateAnalysisService.get_region_wise_engagement')
def test_get_daily_trends_invalid_candidate(mock_get_daily_trends, client):
    mock_data = [{
            "rolling_avg": "52784.00",
            "total_engagement": 52784,
            "tweet_count": 4061,
            "tweet_date": "Thu, 15 Oct 2020 00:00:00 GMT"
        }
    ]
    mock_get_daily_trends.return_value = mock_data
    response = client.get('/api/candidate-analysis/daily-trends?candidate=InvalidCandidate')
    assert response.status_code == 200
    # mock_get_daily_trends.assert_called_with("InvalidCandidate")