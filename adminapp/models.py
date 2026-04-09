from django.db import models

# Create your models here.
class course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=20)
    duration = models.IntegerField()
    fees = models.IntegerField()
    coursedetails = models.CharField(max_length=200)
    courseicon = models.CharField(max_length=60)

class batch(models.Model):
    batchid=models.AutoField(primary_key=True)
    batchtitle=models.CharField(max_length=20)
    batchtime=models.CharField(max_length=20)
    startdate=models.DateField()
    facultyname=models.CharField(max_length=25)
    batchstatus=models.IntegerField()

