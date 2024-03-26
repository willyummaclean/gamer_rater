from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    designer = models.CharField(max_length=155)
    year_released = models.IntegerField(max_length=4)
    players = models.IntegerField(max_length=2)
    completion_time = models.IntegerField(max_length=2)
    min_age = models.ImageField(max_length=2)





#     Table Games {
#   id int pk
#   title varchar
#   description varchar
#   designer varchar
#   year_released number
#   players int
#   completion_time number
#   age number 
# }