from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('log', views.log, name='log'),
    path('validation', views.validation, name='validation'),
    path('modal', views.log, name='register'), 
    path('singup', views.singup, name='singup'), 
    path('singin', views.singin, name='singin'),
    path('onsingup', views.onsingup, name='onsingup'), 
    path('onsingin', views.onsingin, name='onsingin'),
    path('logout', views.logout, name='logout'), 
    path('profil', views.profil, name='profil'), 
    path('contact', views.contact, name='contact'), 
    path('monpannier', views.monpannier, name='monpannier'), 
    path('error', views.error, name='error')
]
