from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
            # + self.first_name + self.last_name


class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owned_barbershop = models.ForeignKey('Barbershop', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.userprofile.first_name + self.user.userprofile.last_name


class Barbershop(models.Model):
    manage_by = models.ForeignKey(User, on_delete=models.CASCADE)
    max_length = 128
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, unique=True)
    picture = models.ImageField(upload_to='shop_profile_images', null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    service = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=300, null=True, blank=True)
    style = models.CharField(max_length=300, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    user_rating = models.IntegerField(null=True, blank=True)
    user_attr = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Barbershop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name