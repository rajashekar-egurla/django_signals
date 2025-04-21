

from django.apps import AppConfig

class Question3SignalTransactionConfig(AppConfig):
    name = 'question3_signal_transaction'

    def ready(self):
        import question3_signal_transaction.signals
