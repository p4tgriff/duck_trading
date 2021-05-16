from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import *


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user_id = User.objects.get(id=request.session['user_id'])
    context = {
        'all_securitys': Security.objects.all(),
        'user_id': user_id,
        'users_id': User.objects.all(),
    }
    return render(request, 'dashboard.html', context)

def returntozero(request):
    return render(request, 'returntozero.html')

def settings(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user_id = User.objects.get(id=request.session['user_id'])
    context = {
        'all_securitys': Security.objects.all(),
        'user_id': user_id,
        'users_id': User.objects.all(),
    }
    return render(request, 'settings.html', context)

def buy(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {}
    return render(request, 'buy.html', context)

def sell(request, security_id):
    if 'user_id' not in request.session:
        return redirect('/')
    a_security = Security.objects.get(id=security_id)
    user_id = User.objects.get(id=request.session['user_id'])
    context = {
        'security': a_security,
        'user_id': user_id
    }
    return render(request, 'sell.html', context)
    # print(request)
    # return render(request, 'sell.html')


def gainloss(request):
    return render(request, 'gainloss.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email_address = request.POST['email_address'])
        request.session['user_id'] = this_user[0].id
        return redirect('/dashboard')
    return redirect('/')

def register(request):

    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')

    if request.method == "POST":

        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], password=hashed_pw
        )
        request.session['user_id'] = new_user.id
    return redirect('/')

def destroy(request, security_id):
    context = {
        'one_security': Security.objects.get(id=security_id)
    }
    return render(request, "returntozero.html", context)

def delete(request, security_id):
    if request.method == 'POST':
        security_to_delete = Security.objects.get(id=security_id)
        security_to_delete.delete()
    return redirect('/dashboard')

def returntozero(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user_id = User.objects.get(id=request.session['user_id'])
    context = {
        'all_securitys': Security.objects.all(),
        'user_id': user_id,
        'users_id': User.objects.all(),
    }
    return render(request, 'returntozero.html', context)

def BankAccount(request):
    return render(request, 'dashboard.html')

def edit(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')
    a_security = Security.objects.get(id=security_id)
    user_id = User.objects.get(id=request.session['user_id'])
    context = {
        'security': a_security,
        'user_id': user_id
    }
    return render(request, "buy.html", context)

def reset(request):
    return render(request, 'dashboard.html')

def update(request, user_id):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/settings')

    to_update = User.objects.get(id=user_id)

    to_update.first_name = request.POST['first_name']
    to_update.last_name = request.POST['last_name']
    to_update.email_address = request.POST['email_address']
    to_update.age = request.POST['age']
    to_update.save()

    return redirect('/dashboard')

def customer(request, pk):
    user = User.objects.get(id=pk)

    orders = user.order_set.all()

    context = {'user': user, 'orders':orders}
    return render(request, 'settings/customer.html', context)

def purchase(request, security_id):
    return render(request, '/')