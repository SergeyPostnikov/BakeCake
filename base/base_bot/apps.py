from django.apps import AppConfig


class BaseBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_bot'
