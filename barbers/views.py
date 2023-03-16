
from barbers.forms import UserForm,UserProfileForm,BarberShopForm
from barbers.models import User;
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.shortcuts import render, redirect


def index(request):
    response = render(request, 'barbers/index.html')
    return response

def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('barbers:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'registration/login.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'registration/registration_form.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})




def barbers(request):
    response = render(request, 'barbers/barbers.html')
    return response


def Add_barber(request):
    registered = False
    manage = request.user
    if request.method == 'POST':
        barber_form = BarberShopForm(request.POST)
        barber_form.manage_by = request.user.username
        if barber_form.is_valid():
            barber = barber_form.save(commit=False)
            barber.manage_by = manage
            barber.save()
        else:
            print(BarberShopForm.errors)
    else:
        barber_form = BarberShopForm()
    return render(request,
                  'barbers/add_barbers.html',
                  context={'barber_form': barber_form,
                           'registered': registered})