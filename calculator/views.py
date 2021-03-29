from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, Http404

# Create your views here.

def home(request):
    return render(request, "calculator/home.html")


# def login(request):
#     return render(request, "registration/login.html")


def login(request):
    return render(request, "calculator/home.html")
