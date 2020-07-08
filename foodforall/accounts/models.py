from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,
         on_delete=models.CASCADE,
    verbose_name="related place",
        )
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    
    def __str__(self):
        return self.user.username

    def create_profile(sender, ** kwarg):
        if kwarg['created']:
            user_profile = UserProfile.objects.create(user=kwarg['instance'])

            post_save.connect(create_profile, sender=User)


#Home page Models

class Carosel(models.Model):
    Caroselimg = models.ImageField(upload_to='carosel_image', blank=True)
    des1 = models.CharField(max_length=100, default='')
    des2 = models.CharField(max_length=100, default='')


