from django.urls import path, include
from home.views import HomeView,postfood, Contact

from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('postfood/',postfood.as_view(), name='post'),
    path('contact/',Contact.as_view(), name='contact'),
]

