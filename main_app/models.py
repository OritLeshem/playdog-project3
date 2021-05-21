from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Event date')
    description = models.TextField(max_length=250)
    location = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name


class Dog(models.Model):
    name=models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    events =models.ManyToManyField(Event)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

    

  
