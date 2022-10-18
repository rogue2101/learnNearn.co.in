
from django.db import models

# Create your models here.

class AddCateg(models.Model):
     categId= models.AutoField(primary_key=True)
     categName=models.CharField(max_length = 100)

     def __str__(self):
          return self.categName

class AddNotes(models.Model):
     nname = models.CharField(max_length = 100)
     ncateg = models.ForeignKey(AddCateg, on_delete=models.CASCADE, null=True)
     ndesc = models.TextField(null=True)
     nimg=models.FileField(upload_to="notes/", max_length=500, null=True, default=None)
     nfile=models.FileField(null=True)

     def __str__(self):
          return self.nname
