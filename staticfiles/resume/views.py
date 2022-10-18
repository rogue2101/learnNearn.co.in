from django.shortcuts import render,redirect
from .models import Profile
from django.http import request,HttpResponse
from django.urls import reverse_lazy
# for download option
from django.template import loader
import pdfkit 
# import io- used for sending and recieving data from user form
import io
import os
# config = pdfkit.configuration(wkhtmltopdf="C:\Users\acer\Downloads\\\\\wkhtmltox-0.12.6-1.msvc2015-win64.exe")


# Create your views here.
def resume_input(request):
    success_url = reverse_lazy('home')

    if request.method=='POST':
      name = request.POST.get('name','')
      phone = request.POST.get('phone','')
      email = request.POST.get('email','')
      school = request.POST.get('school','')
      degree = request.POST.get('degree','')
      university = request.POST.get('university','')
      skill = request.POST.get('skill','')
      about_you = request.POST.get('about_you','')
      previous_work = request.POST.get('previous_work','')

      profile=Profile(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skill=skill,about_you=about_you,previous_work=previous_work)
      profile.save()
    return render(request ,'resume/resume_input.html')


def resume_download(request,id):
  success_url = reverse_lazy('home')

  user_profile=Profile.objects.get(pk=id)
    # template =loader.get_template('resume/resume_download.html')
    # html =template.render({'user_profile':user_profile})
    # option ={
        # 'page-size':'Letter',
        # 'encoding':'UTF-8'
    # }
    # pdf = pdfkit.from_string(html,False,option)
    # response = HttpResponse(pdf,content_type='application/pdf')
    # response['Content-Disposition']='attachment'
    # filename='resume.pdf'
    # return response
  return render(request,'resume/resume_download.html',{'user_profile':user_profile})

def list(request):
    profile = Profile.objects.all()  
    return render(request,'resume/resume_download.html',{'profile':profile})
     
# ====================================



