import os
import time
import logging
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, Http404

# from .models

from django.contrib.auth.models import User


logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    logger.info('At home.!!')
    return render(request, "calculator/home.html")


def calculator(request):
    return render(request, "calculator/calculator.html")


def food(request):
    return render(request, "calculator/calculator.html")


def travel(request):
    return render(request, "calculator/calculator.html")


def households(request):
    return render(request, "calculator/calculator.html")


# def login(request):
#     return render(request, "registration/login.html")


def user(request):
    return render(request, "calculator/user.html")

def users(request):
    users = User.objects.all() 

    return render(request, "calculator/users.html")

def login(request):
    return render(request, "calculator/home.html")

def logout(request):
    return HttpResponse('Good Bye.!')
