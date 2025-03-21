from django.shortcuts import render
from django.views import generic
from .models import Profile

# Create your views here.
class ProfileList(generic.ListView):
    model = Profile
    