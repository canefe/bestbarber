from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput

from barbers.models import UserProfile, Barbershop, Comment,Booking


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('title','first_name','last_name','phoneNumber')
