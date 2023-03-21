from django import forms
from django.contrib.auth.models import User
from barbers.models import  UserProfile
from barbers.models import BarberShop
from barbers.models import Review



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('title','first_name','last_name','phoneNumber')

class AddBarberShopForm(forms.ModelForm):
    class Meta:
        model = BarberShop
        fields = ('name','location','picture','description','service','type','style','price','slug')

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment','rating','shop')
