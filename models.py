from django.db import models


class User(models.Model):
    first_name=models.CharField(null=False,max_length=30,default='kamal')
    last_name=models.CharField(null=False,maxlength=30,default='doe')
    dob = models.DateField(null=True)
