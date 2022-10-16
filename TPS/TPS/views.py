from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

def HomePage(request):
    return render(request ,'home/index3.html')

def about(request):
  return render(request, 'home/about.html')




