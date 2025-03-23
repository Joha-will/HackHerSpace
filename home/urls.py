from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('women_in_tech/', views.women_in_tech, name='women_in_tech'),  # Women in Tech page
    #path('team/', views.team, name='team'),  # Team page
    path('contact/', views.contact, name='contact'),  # Team page
    path('questions/', views.questions, name='questions'),  # Questions page
]