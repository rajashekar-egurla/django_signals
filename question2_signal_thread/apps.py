
from django.apps import AppConfig

class Question2SignalThreadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question2_signal_thread'

    def ready(self):
        import question2_signal_thread.signals
