from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    postfood = models.CharField(max_length=500)
    foodimg = models.ImageField(upload_to='food_image', blank=True)
    fooddes =  models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Carosel(models.Model):
    caroselimg = models.ImageField(upload_to='carosel_image', blank=True)
    des1 = models.CharField(max_length=500)
    des2 = models.CharField(max_length=500)
