from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home_view"),
    path('about', about, name="about"),
]