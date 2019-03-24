from django.conf.urls import url
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('lanny_mode', views.lanny_mode, name='lanny_mode'),
    path('coeur_joie', views.coeur_joie, name='coeur_joie'),



]
