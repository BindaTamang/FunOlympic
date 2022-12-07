from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django_countries.fields import CountryField

from .models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. Add a valid email address')
    country = CountryField().formfield()

    class Meta:
        model = User
        fields = ("full_name", "email", "country", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid email or password')
