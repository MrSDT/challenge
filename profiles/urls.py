from django.urls import path
from . import views
from .views import UserEditProfile

app_name = 'profiles'

urlpatterns = [
    path('users/', views.user_profile, name='userprof'),
    path('profilesettings/', views.UserEditProfile.as_view(), name='UserEditProfile'),
    path('information/', views.information, name='information'),
]