from django import forms

from .models import GameSchedule


class CreateGameSchedule(forms.ModelForm):
    class Meta:
        model = GameSchedule
        fields = ['game', 'date', 'time', 'team1', 'team2']
