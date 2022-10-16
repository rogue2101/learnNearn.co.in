from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings

urlpatterns = [
    path('contact/', views.Contact, name= 'contact'),
   
]