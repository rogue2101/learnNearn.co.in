from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from placement_system.models import student_save,company_jobs,jobapply, stu_appliedjobs

def student_registration(request):
    if request.method=='POST':
        semail = request.POST['semail']
        spassword = request.POST['spassword']
        suser= User.objects.create_user(username = semail,email = semail,password = spassword)
        collage_id = request.POST['collage_id']
        sname = request.POST['sname']
        fname = request.POST['fname']
        mname = request.POST['mname']
        dob = request.POST['dob']
        pnum = request.POST['pnum']
        gender = request.POST['gender']
        state = request.POST['state']
        scity = request.POST['scity']
        pincode = request.POST['pincode']
        
        stu_save = student_save(collage_id=collage_id,sname=sname,fname=fname,mname=mname,dob=dob,pnum=pnum,gender=gender,state=state,scity=scity,pincode=pincode,semail=suser)
        stu_save.save()

        return redirect('student_login')
    return render(request,'registration/student_registration.html')


def logout(request):
    auth.logout(request)
    return render(request, 'home/index3.html')

def student_login(request):
    try:
        if request.method=='POST':
            semail = request.POST['semail']
            spassword = request.POST['spassword']
            student = authenticate(username=semail,password=spassword)
            if student is not None:
                login(request, student)
                return redirect('student_dashboard')

    except:
        pass
    return render(request,'login/student_login.html')



@login_required(login_url='/student_login/')
def student_dashboard(request):
        datashow = student_save.objects.filter(semail = request.user)
        return render(request, 'dashboard/student_dashboard.html',{'data':datashow})

def jobs(request):
    jobshow = company_jobs.objects.all()
    return render(request,'jobs/jobs.html',{'jobs':jobshow})

@login_required(login_url='/student_login/')
def applyjobs(request, id):
   
    jobdetail=company_jobs.objects.filter(id=id)
    datashow = student_save.objects.filter(semail = request.user)
    return render(request,'jobs/applyjobs.html', {'jobdetail' : jobdetail, 'datashow':datashow} )
   
@login_required(login_url='/student_login/')
def submitforjobb(request):
    if request.method=='POST':
        jccode = request.POST['jccode']
        jsname = request.POST['jsname']
        jpnum = request.POST['jpnum']
        jemail= request.POST['jemail']
        jport = request.POST['jport']
        jcurrent = request.POST['jcurrent']
        jreason = request.POST['jreason']
        jsum = request.POST['jsum']
        jresume = request.FILES['jresume']
        

        jobsave = jobapply(jccode=jccode,jsname=jsname,jpnum=jpnum,jemail=jemail,jport=jport,jcurrent=jcurrent,jreason=jreason,jsum=jsum,jresume=jresume)
        jobsave.save()

        stujob=stu_appliedjobs(jscode=jccode,jsemail=jemail)
        stujob.save()
        return redirect('/student_dashboard/')    
    return render(request,'jobs/applyjobs.html')




@login_required(login_url='/student_login/')
def edit_details(request):

    data_show = student_save.objects.filter(semail = request.user)
    if request.method == 'POST':
        pnum = request.POST['pnum']
        state = request.POST['state']
        scity = request.POST['scity']
        pincode = request.POST['pincode']
        hschool = request.POST['hschool']
        hsession = request.POST['hsession']
        hper = request.POST['hper']
        ischool = request.POST['ischool']
        isession = request.POST['isession']
        iper = request.POST['iper']
        lqname = request.POST['lqname']
        lqtype = request.POST['lqtype']
        intname = request.POST['intname']
        intsession = request.POST['intsession']
        intper = request.POST['intper']
        skills = request.POST['skills']

        student_save.objects.filter(semail = request.user).update(pnum=pnum,state=state,scity=scity,pincode=pincode,hschool=hschool,hsession=hsession,hper=hper,ischool=ischool,isession=isession,iper=iper,lqname=lqname,lqtype=lqtype,intname=intname,intsession=intsession,intper=intper,skills=skills)
        return redirect('/student_dashboard/')

    return render(request,'dashboard/editdetails.html',{'data_show':data_show})
