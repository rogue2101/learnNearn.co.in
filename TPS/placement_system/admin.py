from django.contrib import admin
from placement_system.models import student_save, company_jobs, jobapply, stu_appliedjobs

class student_admin(admin.ModelAdmin):
    list_display=('collage_id','sname','fname','mname','dob','pnum','gender','state','scity','pincode','semail','hschool','hsession','hper','ischool','isession','iper','lqname','lqtype','intname','intsession','intper','skills')

admin.site.register(student_save,student_admin)

class jobs_admin(admin.ModelAdmin):
    list_display=('cimg', 'cjob', 'cname', 'cdesc', 'cjobcity', 'cwebsite', 'cemail', 'chrname', 'chrcontact')

admin.site.register(company_jobs,jobs_admin)

class AppliedJobs(admin.ModelAdmin):
    list_display=('jccode','jsname', 'jpnum', 'jemail', 'jport', 'jcurrent', 'jreason', 'jsum', 'jresume')
admin.site.register(jobapply,AppliedJobs)

class StuAppliedJobs(admin.ModelAdmin):
        list_display=('jscode','jsemail')
admin.site.register(stu_appliedjobs,StuAppliedJobs) 