from django.contrib import admin
from barbers.models import BarberShop, UserProfile, Comment


admin.site.register(BarberShop)
admin.site.register(UserProfile)
admin.site.register(Comment)