from django.db import models

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    creation_date = models.DateTimeField()
    votes = models.IntegerField()
            
class Event(models.Model):
    bar = models.ForeignKey(Bar)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
