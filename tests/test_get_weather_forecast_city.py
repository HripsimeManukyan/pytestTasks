import source.weather_forecast  as weather_forecast
import pytest


def test_get_weather_forecast_valid_city():
    assert weather_forecast.get_weather_forecast("Armenia") == "Sunny"


def test_get_weather_forecast_invalid_city():
    assert weather_forecast.get_weather_forecast("Invalid City") =="Unknown"

@pytest.mark.parametrize("city, expected_weather", [
    ("Armenia", "Sunny"),
    ("London", "Rainy"),
    ("Paris", "Unknown")
])

def test_get_weather_forcast_parametrize(city, expected_weather):
    assert weather_forecast.get_weather_forecast(city) == expected_weather

# def test_get_weather_forecast():
#     response = requests.get("https://api.weather.com/forecast")
#     assert response.status_code == 200
#     assert "weather" in response.json()