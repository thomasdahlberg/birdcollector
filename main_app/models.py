from django.db import models
from django.urls import reverse

FOODS = (
    ('M', 'Millet'),
    ('S', 'Suet')
)

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

class Feeding(models.Model):
    date = models.DateField('feeding date')
    food = models.CharField(
        max_length=1,
        choices=FOODS,
        default=FOODS[0][0]
    )
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_food_display()} on {self.date}"