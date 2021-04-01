import os
import time
import logging
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, Http404

logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    logger.info('At home.!!')
    return render(request, "calculator/home.html")


# def login(request):
#     return render(request, "registration/login.html")


def login(request):
    return render(request, "calculator/home.html")
