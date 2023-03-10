from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # school = models.CharField(max_length=50, null=True)
    phoneNumber = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name + self.last_name


class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    manger_name = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.manger_name


class BarberShop(models.Model):
    comment_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE ,null=True)
    manage_by = models.ManyToManyField(ManagerProfile)
    max_length = 128
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, unique=True)
    picture = models.ImageField(upload_to='shop_profile_images', blank=True)
    description = models.CharField(max_length=300)
    service = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    style = models.CharField(max_length=300)
    price = models.FloatField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BarberShop, self).save(*args, **kwargs)

    def __str__(self):
        return self.mana
    
class Review(models.Model):
    comment = models.CharField(max_length=300)
    rating = models.IntegerField()
    shop = models.ForeignKey(BarberShop, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def _str_(self):
        return self.comment
    
class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    shop = models.ForeignKey(BarberShop, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)

    def _str_(self):
        return self.status