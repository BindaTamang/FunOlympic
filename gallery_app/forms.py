from django import forms

from .models import Gallery


class CreateGalleryPostForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image', 'description']
