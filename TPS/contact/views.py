from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.template import loader
from django.contrib import messages
from contact.models import ContactData
from django.conf import settings
# for importing and configuring smtp for sending mails
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.
def Contact(request):
    if request.method=='POST':
        cdname = request.POST['cdname']
        cdemail = request.POST['cdemail']    
        cdsubject = request.POST['cdsubject']
        cdmessage = request.POST['cdmessage']
        # fromemail='fromlearnnearn@gmail.com'
        to='hello.learnnearn@gmail.com'

        html=render_to_string('home/contactform.html', {
            'cdname': cdname,
            'cdemail': cdemail,
            'cdsubject': cdsubject,
            'cdmessage': cdmessage,
        })

        send_mail(
            cdsubject, cdmessage, 'settings.EMAIL_HOST_USER', [to], html_message=html, fail_silently=False
        )
       
       
        # contact = ContactData(cdname=cdname,cdemail=cdemail,cdsubject=cdsubject,cdmessage=cdmessage)
        # contact.save()
        return redirect('home')
    return render(request ,'home/contact.html')