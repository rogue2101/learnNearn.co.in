from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('zoom/', views.current_meeting),
    path('zoom', views.current_meeting, name='current_meeting'),

]