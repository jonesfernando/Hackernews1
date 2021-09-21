from django.conf.urls import url
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=210)
    url=models.URLField(max_length=200)

    #def __str__(self):
      #  return self.add

