from django.db import models


# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

class Cart(models.Model):
    Customer_Email = models.EmailField()
    Seller_Email = models.EmailField()
    Pro_Id = models.IntegerField(default=0)
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Weight = models.IntegerField()
    Weight1 = models.CharField(max_length=10,default=0)
    Sub_Total = models.IntegerField()
    CImage = models.ImageField(upload_to='cart')

class Orders(models.Model):
    Customer_Email = models.EmailField()
    Seller_Email = models.EmailField()
    Pro_Id = models.IntegerField(default=0)
    Order_Id = models.CharField(max_length=50,default="ABC",unique=True)
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Weight = models.IntegerField()
    Weight1 = models.CharField(max_length=10,default=0)
    Sub_Total = models.IntegerField()
    Payment_Mode = models.CharField(default=0,max_length=100)
    Order_Status = models.CharField(max_length=100)
    Order_Date = models.DateTimeField(auto_now=True,auto_now_add=False)
    Status_Date = models.DateTimeField(auto_now=True,auto_now_add=False)
    OImage = models.ImageField(upload_to='orders')




