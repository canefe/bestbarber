
from barbers.forms import LoginForm, UserForm,UserProfileForm
from barbers.models import Barbershop, ManagerProfile, User;
from django.http import HttpResponse, JsonResponse
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
    barbershops = Barbershop.objects.all()
    if request.method == 'POST':
        # check incoming ajax request action if equal to customer
        user = request.user
        if user:
            if request.POST.get('action') == 'customer':
                response_data = {'success': True}
                user.userprofile.completed = True
                user.userprofile.save()
                return JsonResponse(response_data)
            # check incoming ajax request action if equal to barber
            elif request.POST.get('action') == 'barber':
                response_data = {'success': True}
                user.userprofile.completed = True
                manager_profile = ManagerProfile(user=user)
                manager_profile.save()
                user.userprofile.save()
                return JsonResponse(response_data)
    response = render(request, 'barbers/index.html', context={'barbershops': barbershops})
    return response

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.fields['remember_me']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if not remember_me:
                        request.session.set_expiry(0)
                    response_data = {'success': True, 'redirect_url': reverse('barbers:index')}
                    return JsonResponse(response_data)
                else:
                    response_data = {'success': False, 'error': 'Your account is disabled.'}
                    return JsonResponse(response_data)
            else:
                response_data = {'success': False, 'error': 'Your account is disabled.'}
                return JsonResponse(response_data)
    else:
        return render(request, 'registration/login.html', {'form': LoginForm()})


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
            return render(request, 'registration/registration_form.html', {'form': user_form}) 
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()
        

    # Render the template depending on the context.
    return render(request,
                  'registration/registration_form.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


@login_required
def account(request):
    response = render(request, 'barbers/account.html')
    return response

def barbers(request):
    barbershops = Barbershop.objects.all()
    response = render(request, 'barbers/barbers.html', context={'barbershops': barbershops})
    return response
