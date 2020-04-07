from django.db import models
from django.urls import reverse

from datetime import date
from django.contrib.auth.models import User

FOODS = (
    ('M', 'Millet'),
    ('S', 'Suet')
)

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.name}: {self.description}"


class Bird(models.Model):
    sitename = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    count = models.IntegerField()
    gifts = models.ManyToManyField(Gift)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.sitename

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count >= len(FOODS)

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

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url: models.CharField(max_length=200)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bird_id: {self.bird_id} @{bird.url}"
