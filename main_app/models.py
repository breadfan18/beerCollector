from django.db import models
from django.urls import reverse

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
