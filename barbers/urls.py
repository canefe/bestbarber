from django.urls import path
from barbers import views
app_name = 'barbers'
urlpatterns = [
    path('', views.index, name='index'),
    path('barbers', views.barbers, name='barbers'),
]