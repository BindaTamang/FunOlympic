from django.db import models

from home.models import Game


class GameSchedule(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)

    def __str__(self):
        return self.game.name + '-' + self.team1 + 'vs' + self.team2
