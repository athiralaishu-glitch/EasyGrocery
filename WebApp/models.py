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

class CartDB(models.Model):
    Username=models.CharField(max_length=15,null=True,blank=True)
    ProductName=models.CharField(max_length=15,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)
    ProductImage=models.ImageField(upload_to='cart_images',null=True,blank=True)



