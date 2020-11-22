from django.db import models

# Create your models here.

class Product(models.Model):
    Email = models.EmailField()
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Weight = models.IntegerField()
    Weight1 = models.CharField(max_length=10,default=0)
    PImage = models.ImageField(upload_to='Photos')

class Seller(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=20)