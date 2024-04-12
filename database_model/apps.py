from django.apps import AppConfig


class DatabaseModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather_shared_model.database_model'
    verbose_name = 'My Weather Data'  # Customize the display name if desired
