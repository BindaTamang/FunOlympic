from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Video, Comment
from .forms import CreateVideoPostForm, CreateVideoCommentPostForm


def video_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home:home-page')
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'video_app/videos.html', context)


def video_detail(request, id):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('home:home-page')
    video = Video.objects.get(id=id)
    # videos = Video.objects.all()
    videos = Video.objects.all()[:8]
    comments = Comment.objects.filter(video=video)
    context['video'] = video
    context['videos'] = videos
    context['comments'] = comments
    return render(request, 'video_app/video-view.html', context)


def add_video(request):
    context = {}
    user = request.user
    if not user.is_superuser:
        return redirect('home:home-page')

    if request.method == 'POST':
        form = CreateVideoPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video uploaded.')
    else:
        form = CreateVideoPostForm()
    context['form'] = form
    return render(request, "video_app/add-video.html", context)


def add_comment_on_video(request, video_id):
    user = request.user
    if not user.is_authenticated:
        return redirect('home:home-page')

    video = Video.objects.get(id=video_id)
    if request.method == 'POST':
        Comment.objects.create(
            user=user,
            video=video,
            comment=request.POST['comment']
        )
        messages.success(request, 'Comment added.')
    return redirect('video:video-detail', video_id)
