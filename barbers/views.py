from django.utils.decorators import method_decorator
from django.views import View
from barbers.forms import LoginForm, UserForm, UserProfileForm, BarberShopForm, CommentForm, BookingForm, \
    EditBarberShopForm
from barbers.models import User, BarberShop, Comment, UserProfile
from django.http import HttpResponse, JsonResponse
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
                print(114514)
                response_data = {'success': True}
                user.userprofile.completed = True
                user.userprofile.is_barber = True
                user.userprofile.save()
                return JsonResponse(response_data)
    response = render(request, 'barbers/index.html', context=context_dict)
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
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.picture = profile_form.cleaned_data['picture']
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
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('barbers:index'))
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'barbers/profile_registration.html', context_dict)


@login_required
def account(request):
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
                user.userprofile.is_barber = True
                user.userprofile.save()
                return JsonResponse(response_data)
    response = render(request, 'barbers/account.html')
    return response


def barbers(request):
    resetBarber()
    context_dict = {}
    barbers_list = BarberShop.objects.order_by('-name')
    for shop in barbers_list:
        if len(shop.user_attr) > 1:
            shop.user_attr = shop.user_attr.split(",")  # convert user attributes string into list]
        else:
            shop.user_attr = ['?', '?', '?']

    context_dict['barbershops'] = barbers_list

    response = render(request, 'barbers/barbers.html', context=context_dict)
    return response


def show_barber(request, barber_name_slug):
    context_dict = {}

    try:
        barber_form = EditBarberShopForm(request.POST, request.FILES)
        barber = BarberShop.objects.get(slug=barber_name_slug)
        context_dict['barber'] = barber

        comments = Comment.objects.filter(barber_shop=barber)
        context_dict['comments'] = comments
        comment_form = CommentForm(request.POST)
        context_dict['attributes'] = ["Clean",
                                      "Cheap",
                                      "Boring",
                                      "Long_wait",
                                      "Professional",
                                      "Student",
                                      "Fun"
                                      ]

        if request.method == 'POST':
            if comment_form.is_valid():
                if comment_form:
                    comment = comment_form.save(commit=False)
                    attr = request.POST.getlist("attr[]")
                    comment.attr = ','.join(attr)
                    comment.barber_shop = barber
                    comment.user = request.user
                    comment.save()
                    resetBarber()
                    return redirect(reverse('barbers:show_barber',
                                            kwargs={'barber_name_slug':
                                                        barber_name_slug}))
            elif barber_form.is_valid():
                if barber_form:
                    if barber_form.cleaned_data["location"] is not None:
                        barber.location = barber_form.cleaned_data["location"]
                    if barber_form.cleaned_data["picture"] is not None:
                        barber.picture = barber_form.cleaned_data["picture"]
                    if barber_form.cleaned_data["description"] is not None:
                        barber.description = barber_form.cleaned_data["description"]
                    if barber_form.cleaned_data["service"] is not None:
                        barber.service = barber_form.cleaned_data["service"]
                    if barber_form.cleaned_data["type"] is not None:
                        barber.type = barber_form.cleaned_data["type"]
                    if barber_form.cleaned_data["style"] is not None:
                        barber.style = barber_form.cleaned_data["style"]
                    if barber_form.cleaned_data["price"] is not None:
                        barber.price = barber_form.cleaned_data["price"]

                    barber.save()
            else:
                print(barber_form.errors)

        context_dict['comment_form'] = comment_form
        context_dict['barber_form'] = barber_form
    except BarberShop.DoesNotExist:
        context_dict['comments'] = None
        context_dict['barberShop'] = None
    return render(request, 'barbers/show_barber.html', context=context_dict)


def resetBarber():
    barbers = BarberShop.objects.all()

    for barber in barbers:
        comments = Comment.objects.filter(barber_shop=barber)
        rating = 0
        counter = 0
        attr = ""
        for i in comments:
            rating += i.rating
            counter += 1
            if i.attr is not None:
                attr += i.attr + ","
        attr = attr.rstrip(",")
        if (counter != 0):
            barber.user_rating = rating / counter
        else:
            barber.user_rating = 0
        # rating of a barber shop = average comment rating
        attr = {elem: attr.split(",").count(elem) for elem in attr.split(",")}
        attr = dict(sorted(attr.items(), key=lambda x: x[1], reverse=True))
        barber.user_attr = ",".join(list(attr.keys())[:3])
        # read the attributes from Comment
        # 3 attributes with most repetition will be store in barber model
        # update everytime comment is submitted
        barber.save()


def booking(request, barber_name_slug):
    context_dict = {}

    try:
        barber = BarberShop.objects.get(slug=barber_name_slug)
        context_dict['barber'] = barber
        booking_form = BookingForm(request.POST)
        if request.method == 'POST':
            if booking_form.is_valid():
                if booking_form:
                    booking = booking_form.save(commit=False)
                    booking.barber_shop = barber
                    booking.user = request.user
                    booking.save()

                    return redirect(reverse('barbers:show_barber',
                                            kwargs={'barber_name_slug':
                                                        barber_name_slug}))
            else:
                print(booking_form.errors)
        context_dict['booking_form'] = booking_form
        context_dict['barbers'] = barber
    except BarberShop.DoesNotExist:
        context_dict['barbers'] = None
    return render(request, 'barbers/booking.html', context=context_dict)


@login_required
def add_barber(request):
    registered = False

    manage = request.user
    if not manage.userprofile.is_barber:
        return redirect(reverse('barbers:index'))
    if request.method == 'POST':
        barber_form = BarberShopForm(request.POST, request.FILES)
        barber_form.manage_by = request.user
        if barber_form.is_valid():
            barber = barber_form.save(commit=False)
            barber.manage_by = manage
            barber.picture = barber_form.cleaned_data['picture']
            print(barber_form.cleaned_data['picture'])
            barber.user_rating = 0
            barber.save()
            return redirect(reverse('barbers:index'))
        else:
            print("Error")
            print(BarberShopForm.errors)
    else:
        barber_form = BarberShopForm()
    return render(request,
                  'barbers/add_barbers.html',
                  context={'barber_form': barber_form,
                           'registered': registered})


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'picture': user_profile.picture})

        return render(user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('barbers:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        return render(request, 'barbers/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('barbers:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('barbers:profile', user.username)
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        return render(request, 'barbers/profile.html', context_dict)


class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
        profiles = UserProfile.objects.all()
        return render(request, 'barbers/list_profiles.html', {'userprofile_list': profiles})
