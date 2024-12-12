import pytest
from flask import Flask
from app import create_app

# Coverage with respect to: tweet-analysis-app/backend/app/test___init__.py

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

def test_create_app(app):
    assert isinstance(app, Flask)

def test_swagger_ui(client):
    response = client.get("/docs")
    assert response.status_code == 200
    assert b"Swagger UI" in response.data

def test_swagger_yaml(client):
    response = client.get("/static/swagger.yaml")
    assert response.status_code == 200
    assert b"swagger" in response.data

def test_handle_value_error(client):
    @client.application.route("/value_error")
    def value_error_route():
        raise ValueError("This is a test value error")

    response = client.get("/value_error")
    assert response.status_code == 400
    assert response.json == {"error": "This is a test value error"}

def test_handle_generic_exception(client):
    @client.application.route("/generic_exception")
    def generic_exception_route():
        raise Exception("This is a test exception")

    response = client.get("/generic_exception")
    assert response.status_code == 500
    assert response.json == {"error": "An unexpected error occurred.", "details": "This is a test exception"}