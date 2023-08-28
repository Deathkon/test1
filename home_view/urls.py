from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home_view"),
    path('about', about, name="about"),
    path('solution', solution, name="solution"),
    path('contact', contact, name="contact"),
]