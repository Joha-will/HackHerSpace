from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('women-in-tech/', views.women_tech, name='women_tech'),  # Women in Tech page
    path('contact/', views.contact, name='contact'),  # Team page
    path('questions/', views.questions, name='questions'),  # Questions page
]