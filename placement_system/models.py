from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User, auth

class student_save(models.Model):
    collage_id = models.IntegerField()
    sname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    dob = models.DateField()
    pnum = models.IntegerField()
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=60)
    scity = models.CharField(max_length=60)
    pincode = models.IntegerField()
    semail = models.OneToOneField(User,on_delete=models.CASCADE)
    numofjobs=models.IntegerField(default=0)
    
    
    hschool = models.CharField(max_length=50,null=True)
    hsession = models.CharField(max_length=50,null=True)
    hper = models.CharField(max_length=50,null=True)

    ischool = models.CharField(max_length=50,null=True)
    isession = models.CharField(max_length=50,null=True)
    iper = models.CharField(max_length=50,null=True)

    lqname = models.CharField(max_length=50,null=True)
    lqtype = models.CharField(max_length=50,null=True)
    intname = models.CharField(max_length=100,null=True)
    intsession = models.CharField(max_length=50,null=True)
    intper = models.CharField(max_length=50,null=True)

    skills = models.TextField(null=True)

    def __str__(self):
          return self.collage_id

class company_jobs(models.Model):
    cimg=models.FileField(upload_to="jobs/", max_length=500, null=True, default=None)
    cjob=models.CharField(max_length=100)
    cname=models.CharField(max_length=100)
    cdesc=models.TextField()
    cjobcity=models.CharField(max_length=50)
    cwebsite=models.CharField(max_length=100)
    cemail=models.CharField(max_length=100)
    chrname=models.CharField(max_length=50)
    chrcontact=models.CharField(max_length=10)


class jobapply(models.Model):
    jccode=models.CharField(max_length=10)
    jsname=models.CharField(max_length=100)
    jpnum=models.CharField(max_length=100)
    jemail=models.CharField(max_length=100)
    jport=models.CharField(max_length=100)
    jcurrent=models.CharField(max_length=100)
    jreason=models.TextField()
    jsum=models.TextField()
    jresume=models.FileField(upload_to="jobapply/", max_length=500, null=True, default=None)

class stu_appliedjobs(models.Model):
    jscode=models.CharField(max_length=10, null=True)
    jsemail=models.CharField(max_length=50, null=True)
