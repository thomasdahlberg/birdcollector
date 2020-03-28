from django.db import models
from django.urls import reverse

# Create your models here.
class Bird(models.Model):
    sitename = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return self.sitename

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})