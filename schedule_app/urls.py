from django.urls import path

from .views import schedule, add_schedule

app_name = "schedule"
urlpatterns = [
    path('', schedule, name="schedule-all"),
    path('add/', add_schedule, name="schedule-add"),
]