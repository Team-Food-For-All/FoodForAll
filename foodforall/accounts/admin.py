from django.contrib import admin
from accounts.models import UserProfile, Carosel
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Carosel)
admin.site.site_header = 'FoodForAll'

