from django import forms
from django.contrib.auth import get_user_model

from .models import Game

User = get_user_model()


class CreateGamePostForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'image']


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("full_name", "email", "country", "is_verified")
