from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from tzfpy import get_tz
import calendar
from datetime import datetime, date
from .models import WeatherForecast
from .serializers import WeatherForecastSerializer
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API = os.getenv('WEATHER_API')
LOCATION_API = os.getenv('LOCATION_API')
# Default to 5 forecasts
FORECAST_NUM = int(os.getenv('FORECAST_NUM', 5))

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
                # Get day of week
                date_str = data["daily"]["time"][i].split('T')[-1],
                date_object = datetime.strptime(date_str[0], '%Y-%m-%d').date()
                day_of_week = calendar.day_name[date_object.weekday()]
                # Convert 24HR sunrise time to 12HR time
                sunrise = data["daily"]['sunrise'][i].split('T')[-1]
                sunrise_time = datetime.strptime(sunrise, "%H:%M")
                sunrise_time.strftime("%-I:%M")
                sunrise_time_string = sunrise_time.strftime("%-I:%M %p")
                # Convert 24HR sunrise time to 12HR time
                sunset = data["daily"]['sunset'][i].split('T')[-1]
                sunset_time = datetime.strptime(sunset, "%H:%M")
                sunset_time.strftime("%-I:%M")
                sunset_time_string = sunset_time.strftime("%-I:%M %p")
                w = WeatherForecast(
                    # Format date into: Day of Week Month/Day
                    date = day_of_week[0:3] + " " + data["daily"]["time"][i].split('T')[-1].split('-')[-2] 
                            + "/" + data["daily"]["time"][i].split('T')[-1].split('-')[-1],
                    min_temperature = data["daily"]['temperature_2m_min'][i],
                    max_temperature = data["daily"]['temperature_2m_max'][i],
                    precipitation_sum = data["daily"]['precipitation_sum'][i],
                    weathercode = data["daily"]['weathercode'][i],
                    uv_index_max = data["daily"]['uv_index_max'][i],
                    windspeed_10m_max = data["daily"]['windspeed_10m_max'][i],
                    sunrise = sunrise_time_string,
                    sunset = sunset_time_string,
                    # Get feels_like temp based on apparent_temperature_min and apparent_temperature_max
                    feels_like = (data["daily"]['apparent_temperature_min'][i] + data["daily"]['apparent_temperature_max'][i]) // 2
                )
                # Save the forecast to the database
                w.save()
                # Serialize the forecast
                serializer = WeatherForecastSerializer(w)
                forecasts.append(serializer.data)

            return Response(forecasts, status=status.HTTP_200_OK)

        return Response({'error': 'Failed to fetch data from the weather API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except requests.exceptions.RequestException as e:
        return Response({'error': 'Failed to fetch data from the weather API: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
