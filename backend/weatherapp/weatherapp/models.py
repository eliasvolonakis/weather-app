from django.db import models

class WeatherForecast(models.Model):
    date = models.CharField(max_length=10)
    min_temperature = models.DecimalField(max_digits=5, decimal_places=0)
    max_temperature = models.DecimalField(max_digits=5, decimal_places=0)
    precipitation_sum = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    weathercode = models.CharField(max_length=10)
    sunrise = models.CharField(max_length=16)
    sunset = models.CharField(max_length=16)
    uv_index_max = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    windspeed_10m_max = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    def __str__(self):
        return f"{self.date}: MIN: {self.min_temperature} MAX: {self.max_temperature}"
