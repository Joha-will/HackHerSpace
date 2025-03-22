from django.shortcuts import redirect, render, reverse
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User, auth
from .forms import SignInForm, UserSignUpForm

"""
# Create your views here.
class ProfileList(generic.ListView):
    model = User
    template_name = "users/profile_list.html"  # Ensure this template exists

"""

def sign_up(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
    
        else:
            if request.method == "POST":
                form = UserSignUpForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    auth.login(request, user)
                    return redirect(reverse('sign_in'))
            else:
                form = UserSignUpForm()
    except Exception as e:
        print(f"Error occurred while signing up: {e}")
        form = UserSignUpForm()  # Re-render form with error messages for user to correct.

    context = { 'form': form,}

    return render(request, 'users/registration/sign_up.html', context)


def sign_in(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        
        else:
            
            form = SignInForm()

            if request.method == "POST":
                form = SignInForm(request, data=request.POST)
                if form.is_valid():
                    username = request.POST.get('username')
                    password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'users/registration/sign_in.html', {'error': 'Invalid credentials'})

    except Exception as e:
        print(f"Error occurred while signing in: {e}")
        form = SignInForm()
    
    context = { 'form': form,}

    return render(request, 'users/registration/sign_in.html', context)


def sign_out(request):
    auth.sign_out(request)
    return redirect('home')