
from barbers.forms import UserForm,UserProfileForm
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

from barbers.forms import AddBarberShopForm
from barbers.forms import AddReviewForm


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




def barbers(request):
    response = render(request, 'barbers/barbers.html')
    return response

def add_barber(request):
    if request.method == 'POST':
        Addshopform = AddBarberShopForm(request.POST)
        if Addshopform.is_valid():
            Addshopform.save()
            return index(request)
        else:
            print(Addshopform.errors)
    else:
        Addshopform = AddBarberShopForm()
    return render(request, 'barbers/add_barber.html', 
                  context={'Addshopform': Addshopform})

def add_review(request):
    ##we still have to add the user.id which is current user.Not finish yet this part
    if request.method == 'POST':
        ReviewForm = AddReviewForm(request.POST)
        if ReviewForm.is_valid():
            ReviewForm.user = request.user
            ReviewForm.save()
            return index(request)
        else:
            print(ReviewForm.errors)
    else:
        ReviewForm = AddReviewForm()
    return render(request, 'barbers/add_review.html',
                  context={'ReviewForm': ReviewForm})