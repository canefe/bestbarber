from django.contrib import admin
from barbers.models import BarberShop, UserProfile, Comment, Booking


admin.site.register(BarberShop)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Booking)