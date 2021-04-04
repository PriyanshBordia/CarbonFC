import os
import time
import logging
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden, Http404

from . import forms

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


# def addImage(request):
    # pass
    # return render(request, '')


def user(request):
    if request.method == 'POST':
        form = forms.PersonDetailsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "calculator/home.html")
        else:
            return HttpResponse('error')
    else:
        form = forms.PersonDetailsForm()
        print('error2')
    return render(request, "calculator/user.html", {'form': form})
    


def users(request):
    users = User.objects.all() 
    return render(request, "calculator/users.html", context={'users': users})


def login(request):
    return render(request, "calculator/home.html")


def logout(request):
    return HttpResponse('Good Bye.!')
