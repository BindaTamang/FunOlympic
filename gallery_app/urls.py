from django.urls import path

from .views import gallery_view, add_photo

app_name = "gallery"
urlpatterns = [
    path('', gallery_view, name="gallery-view"),
    path('admin-area/add-photo/', add_photo, name="add-photo"),

]