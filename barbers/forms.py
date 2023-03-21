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
        fields = ('title', 'first_name', 'last_name', 'phone_number')


class BarberShopForm(forms.ModelForm):
    class Meta:
        model = BarberShop
        fields = ('name', 'location', 'picture', 'description', 'service', 'type', 'style', 'price')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', 'rating')
