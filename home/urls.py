from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home/templates/home/women_in_tech.html', views.women_tech, name='women_tech')
]