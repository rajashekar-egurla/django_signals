import os
import sys
from django.db import transaction

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_signals.settings')

import django
django.setup()

from question3_signal_transaction.models import DummyModel

try:
    with transaction.atomic():
        DummyModel.objects.create(name='Transaction Test')
        print("[MAIN] Object created.")
        raise Exception("Simulated crash!")
except Exception as e:
    print("[MAIN] Caught exception:", e)

# Check if the object was saved
print("[CHECK] Total objects in DB:", DummyModel.objects.count())
