import pytest
from  rest_framework.test import APIClient
from .models import WeatherForecast
import decimal

client = APIClient()

@pytest.mark.django_db
def test_create_forecast():
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

    
def test_bad_forecast_request_no_locaton():
    response = client.get('/weather/', {}, follow=True)
    assert response.status_code == 404
    