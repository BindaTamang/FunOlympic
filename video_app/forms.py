from django import forms

from .models import Video, Comment


class CreateVideoPostForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'image', 'video_link']


class CreateVideoCommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]
