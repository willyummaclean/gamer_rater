from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    designer = models.CharField(max_length=155)
    year_released = models.IntegerField()
    players = models.IntegerField()
    completion_time = models.IntegerField()
    min_age = models.IntegerField()



