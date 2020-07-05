from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're in mysite project.")

def welcome_user(request, name: str):
    return HttpResponse(f"Hello, {name}. You're in mysite project.")

def calculate_sum(request, first: int, second: int):
    return HttpResponse(first+second)

def calculate_diff(request, first: int, second:int):
    return HttpResponse(first-second)
