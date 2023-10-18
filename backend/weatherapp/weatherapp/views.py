from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from tzfpy import get_tz
from .models import WeatherForecast
from .serializers import WeatherForecastSerializer
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API = os.getenv('WEATHER_API')
LOCATION_API = os.getenv('LOCATION_API')
FORECAST_NUM = int(os.getenv('FORECAST_NUM', 5))  # Default to 5 forecasts

@api_view(['GET'])
def weather_forecast(request, location):
    location_api = LOCATION_API.format(location)
    location_response = requests.get(location_api).json()

    if not location_response:
        return Response({'error': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)

    latitude = location_response[0]['lat']
    longitude = location_response[0]['lon']
    timezone = get_tz(float(longitude), float(latitude))
    weather_api = WEATHER_API.format(timezone, latitude, longitude)

    try:
        weather_response = requests.get(weather_api)

        if weather_response.status_code == 200:
            data = weather_response.json()

            forecasts = []

            for i in range(min(FORECAST_NUM, len(data["daily"]["time"]))):
                w = WeatherForecast(
                    date=data["daily"]["time"][i],
                    min_temperature=data["daily"]['temperature_2m_min'][i],
                    max_temperature=data["daily"]['temperature_2m_max'][i],
                )
                w.save()  # Save the forecast to the database
                serializer = WeatherForecastSerializer(w)  # Serialize the forecast
                forecasts.append(serializer.data)

            return Response(forecasts, status=status.HTTP_200_OK)

        return Response({'error': 'Failed to fetch data from the weather API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except requests.exceptions.RequestException as e:
        return Response({'error': 'Failed to fetch data from the weather API: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
