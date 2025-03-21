from django.shortcuts import render
from django.views import generic
from .models import User

# Create your views here.
class ProfileList(generic.ListView):
    model = User
    template_name = "users/profile_list.html"  # Ensure this template exists
