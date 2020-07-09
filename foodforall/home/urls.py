from django.urls import path, include
from home.views import HomeView,postfood

from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('postfood/',postfood.as_view(), name='post'),
]

