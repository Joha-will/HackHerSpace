from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user



class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )