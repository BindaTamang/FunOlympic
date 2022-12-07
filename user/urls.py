from django.urls import path

from .views import login_view, register_view, logout_view, change_password

app_name = "user"
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('change-password/', change_password, name="change_password"),
]