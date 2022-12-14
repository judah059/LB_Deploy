from django.apps import AppConfig


class OfflinewatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'offlineWatch'

    try:
        import offlineWatch.signals
    except ImportError:
        pass
