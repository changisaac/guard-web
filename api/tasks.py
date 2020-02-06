from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery import shared_task

# custom library imports
from .object_detection.generic_detector import GenericDetector

@shared_task
def process_file(args):
    media_file = str(settings.BASE_DIR) + args['file']
    detector = GenericDetector()
    boxes = detector.get_bounding_boxes(media_file)
    print(boxes)
    return 
