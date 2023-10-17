# myapp/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import WeatherForecast

class WeatherForecastTest(TestCase):
    def setUp(self):
        self.date="2023-10-15"
        self.min_temperature=25.0
        self.max_temperature=30.0
        WeatherForecast.objects.create(
            date="2023-10-15",
            min_temperature=25.0,
            max_temperature=30.0
        )

    def test_weather_data_retrieval(self):
        url = reverse("weather-data", args=(self.date, self.min_temperature, self.max_temperature))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, self.location)
        # Add more assertions based on your view's expected behavior
