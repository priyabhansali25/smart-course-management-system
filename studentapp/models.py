from django.db import models

# Create your models here.
class admission(models.Model):
    admissionno=models.AutoField(primary_key=True)
    batchid=models.IntegerField()
    emailid=models.CharField(max_length=45)
    admissiondate=models.DateField()
