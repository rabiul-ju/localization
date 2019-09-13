from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    url('^$', views.login, name='login'),
    url('registration', views.registration, name='registration'),
    url('home', views.home, name='home'),
    url('logout', views.logout, name='logout'),
    url('asdf', views.change_language, name="change_language")
]
