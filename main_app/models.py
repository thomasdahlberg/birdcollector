from django.db import models

# Create your models here.
class Bird(models.Model):
    sitename = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    count = models.IntegerField()

