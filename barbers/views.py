from barbers.forms import UserForm, UserProfileForm, BarberShopForm, CommentForm
from barbers.models import User, BarberShop, Comment;
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
    barbers_list = BarberShop.objects.order_by('name')

    context_dict = {}
    context_dict['barberShops'] = barbers_list

    visitor_cookie_handler(request)
    response = render(request, 'barbers/index.html', context=context_dict)

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
    barbers_list = BarberShop.objects.order_by('-name')[:5]

    context_dict = {}
    context_dict['barberShops'] = barbers_list

    visitor_cookie_handler(request)
    response = render(request, 'barbers/barbers.html', context=context_dict)

    return response


def show_barber(request, barber_name_slug):
    context_dict = {}

    try:
        barber = BarberShop.objects.get(slug=barber_name_slug)
        context_dict['barber'] = barber

        comments = Comment.objects.filter(barber_shop=barber)
        context_dict['comments'] = comments

        try:
            barber = BarberShop.objects.get(slug=barber_name_slug)
        except BarberShop.DoesNotExist:
            barber = None

        comment_form = CommentForm()
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                if comment_form:
                    comment = comment_form.save(commit=False)
                    comment.barber_shop = barber
                    comment.user = request.user
                    comment.save()
                    return redirect(reverse('barbers:show_barber',
                                            kwargs={'barber_name_slug':
                                                        barber_name_slug}))
            else:
                print(comment_form.errors)

        context_dict['comment_form'] = comment_form
        context_dict['barbers'] = barber
    except BarberShop.DoesNotExist:
        context_dict['comments'] = None
        context_dict['barberShop'] = None

    return render(request, 'barbers/show_barber.html', context=context_dict)


def add_barber(request):
    registered = False
    manage = request.user
    if request.method == 'POST':
        barber_form = BarberShopForm(request.POST)
        barber_form.manage_by = request.user
        if barber_form.is_valid():
            barber = barber_form.save(commit=False)
            barber.manage_by = manage
            barber.save()
            return redirect(reverse('barbers:index'))
        else:
            print(BarberShopForm.errors)
    else:
        barber_form = BarberShopForm()
    return render(request,
                  'barbers/add_barbers.html',
                  context={'barber_form': barber_form,
                           'registered': registered})


def add_comment(request, barber_name_slug):
    return True


# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


# Updated the function definition
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))

    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits
