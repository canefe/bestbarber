from django.contrib import admin
from barbers.models import Barbershop, UserProfile, Comment, Booking


admin.site.register(Barbershop)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Booking)