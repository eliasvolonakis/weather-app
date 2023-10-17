from django.db import models

class WeatherForecast(models.Model):
    date = models.DateField()
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.location} - {self.date}"
