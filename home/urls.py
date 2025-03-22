from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('women-in-tech/', views.women_tech, name='women_tech'),  # Women in Tech page
    path('team/', views.team, name='team'),  # Team page
]