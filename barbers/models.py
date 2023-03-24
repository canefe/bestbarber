from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='user_profile_images', null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True)
    is_barber = models.BooleanField(default=False)
    email = models.CharField(max_length=50, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + self.last_name


class BarberShop(models.Model):
    manage_by = models.ForeignKey(User, on_delete=models.CASCADE)
    max_length = 128
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200,null=True, blank=True, unique=True)
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
        super(BarberShop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber_shop = models.ForeignKey(BarberShop, on_delete=models.CASCADE, null=True, blank=True)
    comment_text = models.CharField(max_length=300, null=True, blank=True)
    rating = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    attr = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.barber_shop.name + self.user.username


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber_shop = models.ForeignKey(BarberShop, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField()
    message = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.user.username + "book" + self.barber_shop.name
