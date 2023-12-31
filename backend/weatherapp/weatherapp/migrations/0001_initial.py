# Generated by Django 3.2.19 on 2023-10-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('min_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
