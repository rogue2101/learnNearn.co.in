from django.db import models


class Meeting_link(models.Model):
    title= models.CharField(max_length=500)
    meeting_id = models.IntegerField(default='')
    meeting_time = models.TimeField(default='12:00:00')
    meeting_date = models.DateField(default='')
    created_by = models.CharField(max_length=50)
    meeting_link = models.URLField(max_length=2000)

    
    def str(self):
        return self.title