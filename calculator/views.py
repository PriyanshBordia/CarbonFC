import os
import time
import logging
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, admin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import PersonDetailsForm
from .models import Person

logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    logger.info('At home.!!')
    return render(request, "calculator/home.html")

@login_required
def calculator(request):
    return render(request, "calculator/calculator.html")

@login_required
def food(request):
    return render(request, "calculator/calculator.html")

@login_required
def travel(request):
    return render(request, "calculator/calculator.html")

@login_required
def households(request):
    return render(request, "calculator/calculator.html")


def personDetails(request, p_id):
    person_details = Person.objects.filter(pk=p_id)
    return render(request, "calculator/person.html", context={'person_details': person_details})


def updatePersonDetails(request, p_id):
    person_details = Person.objects.filter(pk=p_id)
    return render(request, "calculator/person.html")


def allPersons(request):
    user_id = request.user.id
    persons = Person.objects.filter(user=user_id)
    return render(request, "calculator/persons.html")


def updateUserDetails(request):
    if request.method == 'POST':
        form = PersonDetailsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            user_details = Person(pk=request.user.id)
            return render(request, "calculator/user.html")
        else:
            return HttpResponse('error')
    else:
        form = PersonDetailsForm()
        print('error2')
    return render(request, "calculator/user.html", {'form': form})
    

def userDetails(request, user_id):
    user_details = User.objects.filter(pk=user_id)
    return render(request, "calculator/user.html", context={'user_details': user_details})


def allUsers(request):
    users = User.objects.all() 
    return render(request, "calculator/users.html", context={'users': users})


def login(request):
    return render(request, "calculator/home.html")


def logout(request):
    return HttpResponse('Good Bye.!')
