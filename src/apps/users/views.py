from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import LoginForm, RegisterForm


# Create your views here.



def login_user(request: HttpRequest):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('apps.home:list_properties')
            messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")

    context = {
        "form": form
    }
    return render(request, 'users/login.html', context)


def register_user(request: HttpRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('apps.home:list_properties')
        else:
            messages.error(request, "Please correct the errors below.")

    context = {
        "form": form
    }
    return render(request, 'users/register.html', context)




def logout_user(request: HttpRequest):
    logout(request)
    return redirect('apps.home:list_properties')