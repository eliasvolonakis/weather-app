# Generated by Django 3.2.19 on 2023-10-18 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0002_auto_20231018_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherforecast',
            old_name='percipitation_sum',
            new_name='precipitation_sum',
        ),
    ]