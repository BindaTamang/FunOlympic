from django.db import models
from django.contrib.auth import get_user_model

from embed_video.fields import EmbedVideoField

User = get_user_model()


class Video(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    # video_link = models.TextField()
    video_link = EmbedVideoField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
