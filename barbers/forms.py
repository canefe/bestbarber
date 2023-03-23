from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput
from barbers.models import UserProfile, BarberShop, Comment, Booking


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'picture')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)


class BarberShopForm(forms.ModelForm):
    class Meta:
        model = BarberShop
        fields = ('name', 'location', 'picture', 'description', 'service', 'type', 'style', 'price')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', 'rating')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('message', 'date')

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = TextInput(attrs={
            'type': "datetime-local",
            'name': "date",
        })

