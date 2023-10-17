from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import WeatherForecast
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = os.path.join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

WEATHER_API = os.getenv('WEATHER_API')
LOCATION_API = os.getenv('LOCATION_API')

print(WEATHER_API)

class WeatherData():
    def get(self, request, location):
        location_api = LOCATION_API.format(location)
        location_response = requests.get(location_api)
        latitude, longitude = location_response.latitude,location_response.longitude
        weather_api = WEATHER_API.format(timezone, latitude, longitude)
        weather_response = requests.get(weather_api)
        
        if response.status_code == 200:
            data = response.json()
            # Process the data and store it in the database
            print(data)
            # for forecast in data['forecasts']:
            #     WeatherForecast.objects.create(
            #         location=location,
            #         date=forecast['date'],
            #         temperature=forecast['temperature'],
            #         # Add more fields for other weather information as needed
            #     )
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to fetch data from the weather API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
