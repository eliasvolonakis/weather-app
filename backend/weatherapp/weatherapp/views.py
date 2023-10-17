from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import WeatherForecast
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()
# print("WEATHER_API")
WEATHER_API = os.getenv('WEATHER_API')
print(WEATHER_API)
LOCATION_API = os.getenv('LOCATION_API')
FORECAST_NUM = os.getenv('FORECAST_NUM')
print(LOCATION_API)

# WEATHER_API = "https://api.open-meteo.com/v1/forecast?hourly=temperature_2m&timezone={}&latitude={}&longitude={}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
# LOCATION_API = "https://geocode.maps.co/search?q={}"
# location = "Toronto"

print(WEATHER_API)

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def weather_forecast(request, location):
    location_api = LOCATION_API.format(location)
    location_response = requests.get(location_api).json()
    latitude = location_response[0]['lat']
    longitude = location_response[0]['lon']
    timezone = "EST"
    weather_api = WEATHER_API.format(timezone, latitude, longitude)
    weather_response = requests.get(weather_api)
    print(weather_response)
    if weather_response.status_code == 200:
        data = weather_response.json()
        # Process the data and store it in the database
        print(data)
        # Can be changed if more than 5 forecasts are requested
        i = 0
        while i < int(FORECAST_NUM):
            WeatherForecast.objects.create(
                date = str(data["daily"]["time"][i]),
                min_temperature = data["daily"]['temperature_2m_min'][i],
                max_temperature = data["daily"]['temperature_2m_max'][i],
            )
            i += 1
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Failed to fetch data from the weather API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
