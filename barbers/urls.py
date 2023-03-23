from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from barbers import views
from registration.backends.simple.views import RegistrationView
from django.urls import reverse


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('barbers:register_profile')


app_name = 'barbers'
urlpatterns = [
    path('', views.index, name='index'),
    path('account/login/',views.user_login, name = "auth_login"),
    path('account/register/', views.register, name="auth_register"),
    path('barbers', views.barbers, name='barbers'),
    path('register_profile/', views.register, name='register_profile'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('account' , views.account, name='account'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
