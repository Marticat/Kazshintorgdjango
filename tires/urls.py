# tires/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('details/', views.details, name='details'),
]