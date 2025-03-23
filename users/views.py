from django.shortcuts import redirect, render, reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import UserForm



def sign_up(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
    
        elif request.method == 'POST':

            form = UserForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                user = form.save(commit=False)
                user.set_password(password)
                user.role = User.STUDENT
                user.save()
                messages.success(request, 'Your account has been registered successfully!')
                return redirect('register_user')
        else:
            print('invalid form')
            print(form.errors)
    except Exception as e:
        print(f"Error occurred while signing up: {e}")
        form = UserForm()
    context = {
        'form': form,
    }

    return render(request, 'users/registration/sign_up.html', context)


def sign_in(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        
        elif request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'users/registration/sign_in.html', {'error': 'Invalid credentials'})

    except Exception as e:
        print(f"Error occurred while signing in: {e}")

    return render(request, 'users/registration/sign_in.html')


def sign_out(request):
    auth.sign_out(request)
    return redirect('home')






"""
# Create your views here.
class ProfileList(generic.ListView):
    model = User
    template_name = "users/profile_list.html"  # Ensure this template exists

"""