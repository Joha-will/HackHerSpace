from django.urls import path
from . import views

urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('sign_out/', views.sign_out, name="sign_out"),
    path('mentor_sign_up/', views.mentor_sign_up, name="mentor_sign_up"),
    path('dashboard/', views.dashboard, name="dashboard"),
    
]