from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# for possible use of PointField
#from django.contrib.gis.db import models

GENDERS = (
    ('M', 'MALE'),
    ('F', 'FEMALE')
)

SIZES = (
    ('T', 'TINY'),
    ('S', 'SMALL'),
    ('M', 'MEDIUM'),
    ('L', 'LARGE'),
    ('X', 'EXTRA LARGE')
)


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    size = models.CharField(
        max_length=1,
        choices=SIZES,
        default=SIZES[2][0]
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDERS,
        default=GENDERS[0][0]
    )
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

    class Meta:
        ordering = ['name']


class Event(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    date = models.DateField('Event date')
    time = models.TimeField('Event time', default='00:00')
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=150)
    attendees = models.ManyToManyField(Dog)
    lat = models.DecimalField('Latitude', max_digits=9, decimal_places=6)
    lng = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
