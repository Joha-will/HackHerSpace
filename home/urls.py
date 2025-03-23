from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('women-in-tech/', views.women_tech, name='women_tech'),  # Women in Tech page
    path('contact/', views.contact, name='contact'),  # Team page
    path('about/', views.about, name='about'),  # Team page
    path('questions/', views.questions, name='questions'),  # Questions page
    path('mentor/', views.mentor, name='mentor'),  # Mentor page
    
]