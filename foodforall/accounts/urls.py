
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


urlpatterns = [
    
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('register/',views.register, name='register'),
    path('profile/', views.view_profile, name ='view_profile'),
    path('profile/<int:pk>/',views.view_profile, name='view_profile_with_pk'),
    path('foodinfo/<int:pk>/',views.view_profile, name='view_profile_with_pk'),
    path('profile/edit', views.edit_profile, name = "edit_profile"),
    path('change-password/', views.change_password, name ='change_password'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)