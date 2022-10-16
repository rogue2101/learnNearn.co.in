from django.db import models

# Create your models here.
class ContactData(models.Model):
    cdno= models.AutoField(primary_key=True)
    cdname=models.CharField(max_length = 100)
    cdemail = models.CharField(max_length=100)
    cdsubject = models.TextField()
    cdmessage = models.TextField()

    # def __str__(self):
    #     return 'Message from ' + self.cdname + ' - ' +self.cdemail
