from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin' , views.signin , name = "signin"),
    path('login' , views.login , name = "login"),
    path('validation', views.validation, name='validation'),
]
