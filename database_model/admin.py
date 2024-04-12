from django.contrib import admin
from .models import WeatherForecast, WeatherTimeSeries

admin.site.register(WeatherForecast)
admin.site.register(WeatherTimeSeries)
