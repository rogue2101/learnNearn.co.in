from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('notes/', views.Notes, name='notes'),
    path('cat/<int:id>', views.ReadCateg, name='notes-categ'),
    # path('notes/allnotes', views.AllNotes, name='allnotes'),
   
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)