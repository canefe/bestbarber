from barbers.forms import LoginForm, UserForm, UserProfileForm
from django.http import HttpResponse, JsonResponse
from barbers.forms import UserForm, UserProfileForm, BarberShopForm, CommentForm
from barbers.models import User, BarberShop, Comment;
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect


def index(request):
    barbers_list = BarberShop.objects.order_by('name')
    trend_list = BarberShop.objects.order_by('-user_rating')[:6]
    context_dict = {}
    context_dict['barberShops'] = barbers_list
    context_dict['trend_list'] = trend_list

    visitor_cookie_handler(request)
    response = render(request, 'barbers/index.html', context=context_dict)

    return response


def User_login(request):
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

        user_form = UserForm()
        profile_form = UserProfileForm()

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
    context_dict = {}
    barbers_list = BarberShop.objects.order_by('-name')
    for shop in barbers_list:
        if shop.user_attr is not None:
            shop.user_attr = shop.user_attr.split(",")

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
                    attr = request.POST.getlist("attr[]")
                    comment.attr = ','.join(attr)
                    comment.barber_shop = barber
                    comment.user = request.user
                    comment.save()

                    rating = 0
                    counter = 0
                    attr = ""
                    for i in comments:
                        rating += i.rating
                        counter += 1
                        attr += i.attr + ","
                    attr = attr.rstrip(",")
                    barber.user_rating = rating / counter

                    attr = {elem: attr.split(",").count(elem) for elem in attr.split(",")}
                    attr = dict(sorted(attr.items(), key=lambda x: x[1], reverse=True))
                    barber.user_attr = ",".join(list(attr.keys())[:3])

                    barber.save()

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
        barber_form = BarberShopForm(request.POST, request.FILES)
        barber_form.manage_by = request.user
        if barber_form.is_valid():
            barber = barber_form.save(commit=False)
            barber.manage_by = manage
            barber.picture = barber_form.cleaned_data['picture']
            barber.user_rating = 0
            manage.type = "Barber"
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
