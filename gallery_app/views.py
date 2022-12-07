from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Gallery

from .forms import CreateGalleryPostForm


def gallery_view(request):
    photos = Gallery.objects.all()
    context = {
        'photos': photos
    }
    return render(request, "gallery_app/gallery.html", context)


def add_photo(request):
    context = {}
    user = request.user
    if not user.is_superuser:
        return redirect('home:home_page')

    if request.method == 'POST':
        form = CreateGalleryPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'photo added.')
    else:
        form = CreateGalleryPostForm()
    context['form'] = form
    return render(request, "gallery_app/add-photo.html", context)
