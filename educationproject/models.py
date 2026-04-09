from django.db import models


class mstuser(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    gender=models.CharField(max_length=12)
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=60)
    city=models.CharField(max_length=20)
    emailid=models.CharField(max_length=45)
    pwd=models.CharField(max_length=13)
    role=models.CharField(max_length=13)