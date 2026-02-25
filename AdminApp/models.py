from django.db import models

class CategoryDB(models.Model):
    CategoryName=models.CharField(max_length=100,unique=True)
    Description=models.TextField()
    CategoryImage=models.ImageField(upload_to='categories')

    def __str__(self):
        return  self.CategoryName

class ProductDB(models.Model):
    ProductName=models.CharField(max_length=100,unique=True)
    Description=models.TextField()
    Price=models.IntegerField()
    ProductImage=models.ImageField(upload_to='products')
    Category_Name=models.CharField(max_length=100)


class ServicesDB(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField(max_length=300)
    Image=models.ImageField(upload_to='services')