from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Frame(models.Model):
    #doc: https://docs.djangoproject.com/en/3.0/ref/models/fields/#default
    author = models.TextField(default="tiguo")
    start_time = models.TextField(default="0") 
        # or ssJSONField()
    #duration = models.IntegerField()
    road_type = models.CharField(max_length=25, default="", db_index=True)
    gps_lag = models.FloatField(default=0, db_index=True)
    gps_long = models.FloatField(default=0, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    car = models.IntegerField(default=0, db_index=True)
    bike = models.IntegerField(default=0, db_index=True)
    man = models.IntegerField(default=0, db_index=True)



class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
