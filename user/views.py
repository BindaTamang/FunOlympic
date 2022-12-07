from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django_countries import countries

from .forms import RegistrationForm, AccountAuthenticationForm


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hurray! You are now registered user.')
    else:
        form = RegistrationForm()
    context = {
        "registration_form": form,
        "countries": list(countries)
    }
    return render(request, "user/register.html", context)


def login_view(request):
    context = {}

    if request.user.is_authenticated:
        return redirect("home:home-page")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home:home-page")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home:home-page')


def change_password(request):
    user = request.user
    if not user.is_authenticated:
        return  redirect("home:home-page")
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user:change_password')
        # else:
        #     messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change-password.html', {
        'form': form
    })
