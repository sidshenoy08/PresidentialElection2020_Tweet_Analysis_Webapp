import pytest
from unittest.mock import patch
from app import create_app
from app.modules.geographic_analysis.controller.GeographicAnalysisController import GeographicAnalysisController
# Tests for File: tweet-analysis-app/backend/app/modules/geographic_analysis/controller/test_GeographicAnalysisController.py

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

@patch('app.modules.geographic_analysis.controller.GeographicAnalysisController.GeographicAnalysisService.get_most_tweets_by_country')
def test_get_most_tweets_by_country(mock_get_most_tweets_by_country, client):
    mock_data = [
        {
        "country": "United Kingdom",
        "tweet_count": 29554
    }
    ]
    mock_get_most_tweets_by_country.return_value = mock_data
    response = client.get('/api/geographic-analysis/most-tweets-by-country')
    assert response.status_code == 200
    assert response.json == mock_data


@patch('app.modules.geographic_analysis.controller.GeographicAnalysisController.GeographicAnalysisService.get_city_level_analysis')
def test_get_city_level_analysis(mock_get_city_level_analysis, client):
    mock_data = [
        {
        "city": "New York",
        "likes": 1392284,
        "retweets": 277991,
        "tweet_count": 33724
    }
    ]
    mock_get_city_level_analysis.return_value = mock_data
    response = client.get('/api/geographic-analysis/city-level-analysis')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.geographic_analysis.controller.GeographicAnalysisController.GeographicAnalysisService.get_top_tweets_by_region')
def test_get_top_tweets_by_region(mock_get_top_tweets_by_region, client):
    mock_data = [
       {
        "likes": 165702,
        "location": "New York, New York, United States of America",
        "retweet_count": 17652,
        "tweet": "Tonight a woman in the audience of Trump's town hall began her question by telling him he has a great smile &amp; he's so handsome when he smiles. And when #JoeBiden is President, hopefully that woman will be able to access better vision care, bless her heart.",
        "tweet_id": 1316941303603728384,
        "user_name": "bettemidler"
    }
    ]
    mock_get_top_tweets_by_region.return_value = mock_data
    response = client.get('/api/geographic-analysis/top-tweets-by-region')
    assert response.status_code == 200
    assert response.json == mock_data

@patch('app.modules.geographic_analysis.controller.GeographicAnalysisController.GeographicAnalysisService.get_engagement_by_timezone')
def test_get_engagement_by_timezone(mock_get_engagement_by_timezone, client):
    mock_data = [
        {
        "likes": 868641,
        "retweets": 202249,
        "time_zone": "America/New_York",
        "tweet_count": 45500
    }
    ]
    mock_get_engagement_by_timezone.return_value = mock_data
    response = client.get('/api/geographic-analysis/engagement-by-timezone')
    assert response.status_code == 200
    assert response.json == mock_data