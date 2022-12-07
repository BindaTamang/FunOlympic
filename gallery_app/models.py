from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField()
