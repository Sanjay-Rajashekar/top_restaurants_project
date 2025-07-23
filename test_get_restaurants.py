import pytest
import requests
import requests_mock
from top_restaurants import validate_city, get_top_restaurants

API_KEY = "test_api_key"

def test_validate_city_success(requests_mock):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    mocked_response = {
        "candidates": [{"formatted_address": "Bangalore, Karnataka, India"}],
        "status": "OK"
    }
    requests_mock.get(url, json=mocked_response)
    assert validate_city("Bangalore", API_KEY) == True

def test_validate_city_failure(requests_mock):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    mocked_response = {
        "candidates": [],
        "status": "ZERO_RESULTS"
    }
    requests_mock.get(url, json=mocked_response)
    assert validate_city("InvalidCityName", API_KEY) == False

def test_get_top_restaurants_success(requests_mock):
    # Mock validate_city to return True
    import top_restaurants
    def mock_validate_city(city, api_key):
        return True
    top_restaurants.validate_city = mock_validate_city

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    mocked_response = {
        "results": [
            {
                "name": "Test Restaurant",
                "rating": 4.5,
                "user_ratings_total": 100,
                "formatted_address": "Test Address"
            }
        ]
    }
    requests_mock.get(url, json=mocked_response)
    data = top_restaurants.get_top_restaurants("Bangalore", API_KEY)
    assert "Test Restaurant" in data
    assert data["Test Restaurant"]["rating"] == 4.5


def test_get_top_restaurants_invalid_city(monkeypatch):
    # Mock validate_city to return False
    from top_restaurants import validate_city
    def mock_validate_city(city, api_key):
        return False
    monkeypatch.setattr("top_restaurants.validate_city", mock_validate_city)

    data = get_top_restaurants("InvalidCity", API_KEY)
    assert data == {}

def test_get_top_restaurants_connection_error(monkeypatch):
    def mock_requests_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError
    monkeypatch.setattr(requests, "get", mock_requests_get)

    data = get_top_restaurants("Bangalore", API_KEY)
    assert data == {}
