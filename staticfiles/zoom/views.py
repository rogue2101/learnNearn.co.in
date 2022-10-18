# Create your views here.
from django.shortcuts import render
from datetime import datetime
from .models import Meeting_link

def current_meeting(request):
    datashow = Meeting_link.objects.all()
    
    if current_meeting==None:
        return render(request,'zoom/nomeeting.html')

    else:
        return render(request,'zoom/zoom_link.html',{'data':datashow})