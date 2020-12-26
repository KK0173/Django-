from datetime import timezone

from django.db import models

# Create your models here.
import datetime
now_time = datetime.datetime.now()

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20,default=0)
    token=models.CharField(max_length=250,default='')
    class Meta:
        db_table = 'user_data'

class Post(models.Model):
    time = models.CharField(max_length=20,default=now_time)
    address = models.CharField(max_length=20,default='')
    discription=models.CharField(max_length=20,default='')

    class Meta:
        db_table = 'user_post'