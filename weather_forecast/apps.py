from django.apps import AppConfig
import os


class WeatherForecastConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    if 'weather_shared_model' in os.getcwd():
        print('We are INSIDE the weather_shared_model')
        name = 'weather_forecast' # works for migrations INSIDE the submodule
    else:
        print('We are OUTSIDE the weather_shared_model')
        name = 'weather_shared_model.weather_forecast' # works for migrations OUTSIDE the submodule
    
    verbose_name = 'Weather Forecast'  # Customize the display name if desired
