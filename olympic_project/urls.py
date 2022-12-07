from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static, serve

patterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls", namespace="home")),
    path('user/', include("user.urls", namespace="user")),
    path('gallery/', include("gallery_app.urls", namespace="gallery")),
    path('video/', include("video_app.urls", namespace="video")),
    path('schedule/', include("schedule_app.urls", namespace="schedule")),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    staticpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
                     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    staticpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns = patterns + staticpatterns
