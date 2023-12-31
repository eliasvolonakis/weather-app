# Generated by Django 3.2.19 on 2023-10-19 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0003_rename_percipitation_sum_weatherforecast_precipitation_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherforecast',
            name='sunrise',
            field=models.CharField(default='7:00', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='sunset',
            field=models.CharField(default='20:00', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='uv_index_max',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='weathercode',
            field=models.CharField(default='80', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='windspeed_10m_max',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='weatherforecast',
            name='max_temperature',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='weatherforecast',
            name='min_temperature',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
