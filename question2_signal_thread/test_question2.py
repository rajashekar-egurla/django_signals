
import threading
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_signals.settings')

import django
django.setup()

from question2_signal_thread.models import DummyModel
import time

def create_dummy_model():
    print("Thread started:", threading.current_thread().name)
    DummyModel.objects.create(name='Thread Test')
    print("Thread ended:", threading.current_thread().name)

if __name__ == "__main__":
    print("Main thread:", threading.current_thread().name)

    
    thread = threading.Thread(target=create_dummy_model)
    thread.start()
    thread.join()

    print("Main thread finished.")
