from django.db import models

class WeatherForecast(models.Model):
    date = models.CharField(max_length=10)
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation_sum = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.date}: MIN: {self.min_temperature} MAX: {self.max_temperature}"
