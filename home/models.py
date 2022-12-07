from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='games/')

    def __str__(self):
        return self.name
