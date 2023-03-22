from django import forms
from django.contrib.auth.models import User
from barbers.models import UserProfile, BarberShop, Comment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','phone_number')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

class BarberShopForm(forms.ModelForm):
    class Meta:
        model = BarberShop
        fields = ('name', 'location', 'picture', 'description', 'service', 'type', 'style', 'price')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', 'rating')

