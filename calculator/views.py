import os
import time
import logging
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, admin_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
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
    # person_details = Person.objects.filter(pk=p_id)
    return HttpResponseRedirect(reverse("person", args=(p_id, )))


def allPersons(request):
    user_id = request.user.id
    persons = Person.objects.filter(user=user_id)
    return render(request, "calculator/persons.html")


def userDetails(request, user_id):
    user_details = User.objects.get(pk=user_id)
    print(user_details)
    return render(request, "calculator/user.html", context={'user_details': user_details})


def updateUserDetails(request):
    user_id = request.user.id
    try:
        first_name = str(request.POST.get("first_name"))
    except KeyError:
        return render(request, "calculator/error.html", context={"message":  "Enter a First Name!!", "type": "Key Error!!"})
    except ValueError:
        return render(request, "calculator/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
    except TypeError:
        return render(request, "calculator/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!",})

    try:
        last_name = str(request.POST.get("last_name"))
    except KeyError:
        return render(request, "calculator/error.html", context={"message":  "Enter a Last Name!!", "type": "Key Error!!"})
    except ValueError:
        return render(request, "calculator/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
    except TypeError:
        return render(request, "calculator/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!",})

    try:
        email = str(request.POST.get("email"))
    except KeyError:
        return render(request, "calculator/error.html", context={"message": "Enter a e-mail address!!", "type": "KeyError!!"})
    except ValueError:
        return render(request, "calculator/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
    except TypeError:
        return render(request, "calculator/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!",})

    try:
        user_details = User.objects.get(pk=user_id)
        if user_details != None:
            user_details.first_name = first_name
            user_details.last_name = last_name
            user_details.email = email
            user_details.save()
    except ValueError:
        return render(request, "calculator/error.html", context = {"message": "User Doesn't Exist!", "type": "Value DoesNotExist.!!", })


    # if request.method == 'POST':
    #     form = PersonDetailsForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         form.save()
    #         user_details = Person(pk=request.user.id)
    #         return render(request, "calculator/user.html")
    #     else:
    #         return HttpResponse('error')
    # else:
    #     form = PersonDetailsForm()
    #     print('error2')
    return HttpResponseRedirect(reverse("user", args=(user_id, )))


def allUsers(request):
    users = User.objects.all() 
    return render(request, "calculator/users.html", context={'users': users})


def login(request):
    return render(request, "calculator/home.html")


def logout(request):
    return HttpResponse('Good Bye.!')
