from django.db import models


class Post(models.Model):
    farm_num = models.TextField(max_length=100, blank=True, null=True)
    farm_name = models.CharField(max_length=100, null=True, default='None')
    lat = models.FloatField(max_length=100, blank=True, null=True)
    long = models.FloatField(max_length=100, blank=True, null=True)
    distance = models.FloatField(max_length=100, blank=True, null=True)
    result = models.FloatField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'[{self.pk}] 농장이름 :: {self.farm_name}'


