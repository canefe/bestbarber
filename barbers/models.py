from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=6, default="User")
    email = models.CharField(max_length=50, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + self.last_name


class BarberShop(models.Model):
    manage_by = models.ForeignKey(User, on_delete=models.CASCADE)
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
        super(BarberShop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber_shop = models.ForeignKey(BarberShop, on_delete=models.CASCADE, null=True, blank=True)
    comment_text = models.CharField(max_length=300, null=True, blank=True)
    rating = models.IntegerField()
    attr = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.barber_shop.name + self.user.username
