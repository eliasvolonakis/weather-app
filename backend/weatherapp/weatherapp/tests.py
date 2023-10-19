import pytest
from  rest_framework.test import APIClient
from .models import WeatherForecast
import decimal
import os
import warnings

os.environ["DJANGO_SETTINGS_MODULE"] = "weatherapp.settings"
client = APIClient()

@pytest.mark.django_db
def test_create_forecast():
    warnings.simplefilter("ignore")
    response = client.get('/weather/Toronto', {}, follow=True)
    assert response.status_code == 200
    forecast = WeatherForecast.objects.first()
    assert forecast is not None
    assert forecast.date is not None
    assert type(forecast.date) is str
    assert forecast.min_temperature is not None
    assert type(forecast.min_temperature) is decimal.Decimal
    assert forecast.max_temperature is not None
    assert type(forecast.max_temperature) is decimal.Decimal
    assert forecast.precipitation_sum is not None
    assert type(forecast.precipitation_sum) is decimal.Decimal
    assert type(forecast.weathercode) is str
    assert forecast.weathercode is not None
    assert type(forecast.sunrise) is str
    assert forecast.uv_index_max is not None
    assert type(forecast.uv_index_max) is decimal.Decimal
    assert forecast.windspeed_10m_max is not None
    assert type(forecast.windspeed_10m_max) is decimal.Decimal

    
def test_bad_forecast_request_no_locaton():
    warnings.simplefilter("ignore")
    response = client.get('/weather/', {}, follow=True)
    assert response.status_code == 404
    
def test_bad_forecast_request_invalid_locaton():
    warnings.simplefilter("ignore")
    response = client.get('/weather/Toronto2', {}, follow=True)
    assert response.status_code == 404
    