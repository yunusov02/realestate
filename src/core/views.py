from django.shortcuts import render
from django.http import HttpResponse, HttpRequest



def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'landing.html')