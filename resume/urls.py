from django.urls import include, path
from django.contrib import admin
from . import views
urlpatterns = [

    path('resume', views.resume_input, name='resume_input'),
    path('resume/<int:id>/', views.resume_download, name='resume_download'),
    path('resume_download/<int:id>/', views.resume_download, name='resume_download'),

 ]