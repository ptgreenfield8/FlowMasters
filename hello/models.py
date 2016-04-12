from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
class Datapoint(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
