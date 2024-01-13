from django.db import models
from django.urls import reverse

class Event(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    live_url = models.URLField()

    def __str__(self):
        return self.title

    
