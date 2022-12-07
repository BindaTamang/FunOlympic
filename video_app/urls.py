from django.urls import path

from .views import video_view, add_video, video_detail, add_comment_on_video

app_name = "video"
urlpatterns = [
    path('', video_view, name="video-view"),
    path('add/', add_video, name="video-add"),
    path('<int:id>/', video_detail, name="video-detail"),
    path('comment/<int:video_id>/', add_comment_on_video, name="add_comment_on_video"),
]
