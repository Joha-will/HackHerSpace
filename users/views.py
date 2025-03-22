from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import User
from .forms import UserSignUpForm

# Create your views here.
class ProfileList(generic.ListView):
    model = User
    template_name = "users/profile_list.html"  # Ensure this template exists


class SignUpView(generic.CreateView):
    form_class = UserSignUpForm
    template_name = "users/registration/sign_up.html"
    success_url = reverse_lazy("sign_in")