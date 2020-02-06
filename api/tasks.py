from __future__ import absolute_import
from celery import shared_task
import time

@shared_task  # Use this decorator to make this a asyncronous function
def test_celery():
    time.sleep(5)
    print('TASK TESTING')
    return
    
