from django import forms
from .models import User, Mentor



class UserForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password',)

    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')



class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('mentor_name', 'mentor_certificate',)