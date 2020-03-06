from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Frame(models.Model):
    #doc: https://docs.djangoproject.com/en/3.0/ref/models/fields/#default
    #add an primary key for??? AutoField(**options)
         #???An IntegerField that automatically increments according to available IDs. You usually won’t need to use this directly; a primary key field will automatically be added to your model if you don’t specify otherwise. See Automatic primary key fields.
    author = models.TextField(default="tiguo")
    start_time = models.TextField(default="0") 
        # or ssJSONField()
        # use db_index? (If True, a database index will be created for this field.)
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
