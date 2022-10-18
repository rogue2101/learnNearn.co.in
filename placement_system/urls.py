import imp
from xml.dom.minidom import Document
from django.urls import include, path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('student_registration/', views.student_registration,name='student_registration'),

path('student_login/', views.student_login,name='student_login'),

path('/', views.logout, name='logout'),


path('student_dashboard/', views.student_dashboard,name='student_dashboard'),

path('edit_details/', views.edit_details, name='edit_details'),



path('jobs/', views.jobs, name='jobs'),

path('jobs/applyjobs/<int:id>', views.applyjobs, name='applyjobs'),

path('submitforjobb/', views.submitforjobb, name='submitforjobb'),



]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)