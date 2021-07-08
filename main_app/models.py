from django.db import models
from django.urls import reverse

DRINKS = (
    ('M', 'Morning Drink')
    ('A', 'Afternoon Drink')
    ('N', 'Night Drink')
)

# Create your models here.
class Beer(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    alcPercent = models.CharField(max_length=10)
    abuLevel = models.IntegerField()
    origin = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'beer_id': self.id})

class Drinking(models.Model):
    date = models.DateField()
    drink = models.CharField(
        max_length=1,
        choices=DRINKS,
        # default sets the defauly value to the first one, which is M in DRINKS
        default=DRINKS[0][0]
    )

    def __str__(self) -> str:
        return f'{self.get_drink_display()} on {self.date}'