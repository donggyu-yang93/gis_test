from django.db import models


class Post(models.Model):
    farm_num = models.TextField(max_length=100, blank=True, null=True)
    farm_name = models.CharField(max_length=100, null=True, default='None')
    lat = models.TextField(max_length=100, blank=True, null=True)
    long = models.TextField(max_length=100, blank=True, null=True)
    distance = models.TextField(max_length=100, blank=True, null=True)
    result = models.TextField(max_length=100, blank=True, null=True)

# Create your models here.
