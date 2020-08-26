from django.urls import path, include
from home.views import HomeView,postfood, Contact, About, Event, FoodInfo

from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('postfood/',postfood.as_view(), name='post'),
    path('contact/',Contact.as_view(), name='contact'),
    path('about/',About.as_view(), name='about'),
    path('event/',Event.as_view(), name='event'),
    path('foodinfo/',FoodInfo.as_view(), name='foodinfo'),
   
]

