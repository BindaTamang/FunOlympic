from django.shortcuts import render, redirect
from django.contrib import messages

from .models import GameSchedule, Game
from .forms import CreateGameSchedule

def schedule(request):
    game_schedule = GameSchedule.objects.all()
    context = {
        "game_schedule": game_schedule
    }
    return render(request, 'schedule_app/schedule.html', context)

def add_schedule(request):
    context = {}
    user = request.user
    if not user.is_superuser:
        return redirect('home:home_page')

    if request.method == 'POST':
        form = CreateGameSchedule(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Game Schedule added.')
    else:
        games = Game.objects.all()
        form = CreateGameSchedule()
        context['games'] = games
    context['form'] = form
    return render(request, 'schedule_app/add-schedule.html', context)