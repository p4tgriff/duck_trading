from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import *


def index(request):
    # request.session.flush()
    return render(request, 'index.html')

def dashboard(request):
    # request.session.flush()
    return render(request, 'dashboard.html')

def returntozero(request):
    # request.session.flush()
    return render(request, 'returntozero.html')

def settings(request):
    # request.session.flush()
    return render(request, 'settings.html')

def buy(request):
    # request.session.flush()
    return render(request, 'buy.html')

def sell(request):
    # request.session.flush()
    return render(request, 'sell.html')

def gainloss(request):
    # request.session.flush()
    return render(request, 'gainloss.html')
