from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Message=models.TextField()

class SignupDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Password=models.CharField(max_length=25)
    Confirm_Password=models.CharField(max_length=25)


