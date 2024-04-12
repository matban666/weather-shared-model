from django.db import models

class WeatherForecast(models.Model):
    model_run_date = models.DateTimeField(verbose_name="Model Run Date")

class WeatherTimeSeries(models.Model):
    forecast = models.ForeignKey(WeatherForecast, on_delete=models.CASCADE, related_name="time_series")
    time = models.DateTimeField()
    screen_temperature = models.FloatField(verbose_name="Screen Temperature")
    max_screen_air_temp = models.FloatField(verbose_name="Max Screen Air Temp", null=True)
    min_screen_air_temp = models.FloatField(verbose_name="Min Screen Air Temp", null=True)
    screen_dew_point_temperature = models.FloatField(verbose_name="Screen Dew Point Temperature")
    feels_like_temperature = models.FloatField(verbose_name="Feels Like Temperature")
    wind_speed_10m = models.FloatField(verbose_name="Wind Speed (10m)")
    wind_direction_from_10m = models.IntegerField(verbose_name="Wind Direction (10m)")
    wind_gust_speed_10m = models.FloatField(verbose_name="Wind Gust Speed (10m)")
    max_10m_wind_gust = models.FloatField(verbose_name="Max Wind Gust (10m)", null=True)
    visibility = models.IntegerField()
    screen_relative_humidity = models.FloatField(verbose_name="Screen Relative Humidity")
    mslp = models.IntegerField()
    uv_index = models.IntegerField(verbose_name="UV Index")
    significant_weather_code = models.IntegerField(verbose_name="Significant Weather Code")
    precipitation_rate = models.IntegerField(verbose_name="Precipitation Rate")
    total_precip_amount = models.IntegerField(verbose_name="Total Precipitation Amount", null=True)
    total_snow_amount = models.IntegerField(verbose_name="Total Snow Amount", null=True)
    prob_of_precipitation = models.IntegerField(verbose_name="Probability of Precipitation")
