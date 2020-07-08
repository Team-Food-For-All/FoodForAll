from django.urls import path, include
from home.views import HomeView

from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

