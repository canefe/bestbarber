from django.contrib import admin
from barbers.models import Barbershop, UserProfile, ManagerProfile


admin.site.register(Barbershop)
admin.site.register(UserProfile)
admin.site.register(ManagerProfile)