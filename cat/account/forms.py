from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password',]
