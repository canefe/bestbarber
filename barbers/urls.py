from django.urls import path
from barbers import views


app_name = 'barbers'
urlpatterns = [
    path('', views.index, name='index'),
    path('account/login/',views.User_login, name = "auth_login"),
    path('account/register/', views.register, name="auth_register"),
    path('barbers/', views.barbers, name='barbers'),
    path('add_barbers/', views.add_barber, name='add_barbers'),
    path('barber/<slug:barber_name_slug>/',
         views.show_barber, name='show_barber'),

]