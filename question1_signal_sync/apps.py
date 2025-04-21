from django.apps import AppConfig

class Question1SignalSyncConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question1_signal_sync'

    def ready(self):
        import question1_signal_sync.signals
