
import sys
import os
import django
import time



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_signals.settings')


django.setup()

from question1_signal_sync.models import DummyModel

print("Before save")
start = time.time()
DummyModel.objects.create(name='Test')
print("After save")
print("Time taken:", time.time() - start)
