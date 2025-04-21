
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DummyModel
import threading

@receiver(post_save, sender=DummyModel)
def dummy_model_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Signal triggered in thread: {threading.current_thread().name}")
