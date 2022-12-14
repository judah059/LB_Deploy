from django.apps import AppConfig


class OfflinewatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'offlineWatch'

    def ready(self):
        try:
            import offlineWatch.signals
        except ImportError:
            pass
