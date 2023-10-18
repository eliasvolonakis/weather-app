from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import WeatherForecast
from unittest.mock import patch, Mock
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from tzfpy import get_tz
import pytest
from  rest_framework.test import APIClient
from .models import WeatherForecast

client = APIClient()

@pytest.mark.django_db
def test_create_forecast():
    response = client.get('/weather/Toronto', {}, follow=True)
    assert response.status_code == 200
    forecast = WeatherForecast.objects.first()
    assert forecast is not None
    
def test_bad_forecast_request_no_locaton():
    response = client.get('/weather/', {}, follow=True)
    assert response.status_code == 404
    