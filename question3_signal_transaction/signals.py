from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DummyModel

@receiver(post_save, sender=DummyModel)
def signal_handler(sender, instance, created, **kwargs):
    print(f"[SIGNAL] DummyModel with name '{instance.name}' was saved.")
