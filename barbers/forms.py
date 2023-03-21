from django import forms
from django.contrib.auth.models import User
from barbers.models import  UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
   
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','phone_number')

# make a django login form using username and password only