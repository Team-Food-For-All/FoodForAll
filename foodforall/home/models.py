from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    postfood = models.CharField(max_length=500)
    foodimg = models.ImageField(upload_to='food_image', blank=True)
    fooddes = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Carosel(models.Model):
    caroselimg = models.ImageField(upload_to='carosel_image', blank=True)
    des1 = models.CharField(max_length=500)
    des2 = models.CharField(max_length=500)


class Partner(models.Model):
    partnerimg = models.ImageField(upload_to='partner_image', blank=True)
    partnername = models.CharField(max_length=500)
    partnerdes = models.CharField(max_length=500)


class Donater(models.Model):
    donaterimg = models.ImageField(upload_to='donater_image', blank=True)
    donaterdes = models.TextField(max_length=500)
    donaterlocation = models.CharField(max_length=500)
    donatername = models.CharField(max_length=500)


class Subcriber(models.Model):
    subcriber = models.EmailField(max_length=500)

    def __str__(self):
        return self.subcriber


class Contactinfo(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class EventInfo(models.Model):
    eventname = models.CharField(max_length=500)
    eventimg = models.ImageField(upload_to='Event_image', blank=True)
    eventdes = models.CharField(max_length=500)
    eventlocation = models.CharField(max_length=500)
    eventcontact = models.IntegerField(default=0)
    date = models.DateTimeField()
    uploaddate = models.DateTimeField(auto_now=True)
