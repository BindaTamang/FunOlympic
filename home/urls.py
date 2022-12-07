from django.urls import path

from .views import home_page, about_us, admin_area, add_game, all_games, user_list, delete_user, edit_user

app_name = "home"
urlpatterns = [
    path('', home_page, name="home-page"),
    path('about-us/', about_us, name="about-us"),
    path('admin-area/', admin_area, name="admin-area"),
    path('add-game/', add_game, name="add-game"),
    path('game/', all_games, name="game"),
    path('user-list/', user_list, name="user-list"),
    path('user/delete/<int:user_id>/', delete_user, name="user-delete"),
    path('user/edit/<int:user_id>/', edit_user, name="user-edit"),
]