from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=15,blank=True)
    aline1=models.CharField(max_length=20,null=True)
    aline2=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username

class products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate=models.CharField(max_length=30)
    productname=models.CharField(max_length=40,null=True)
    productimage=models.FileField(null=True)
    category=models.CharField(max_length=30,null=True)
    productprice=models.PositiveIntegerField(null=True)
    brand=models.CharField(max_length=20)
    description=models.CharField(max_length=750)

    def __str__(self):
        return self.productname

class category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate=models.CharField(max_length=30)
    categoryname=models.CharField(max_length=40,null=True)
    categoryimage=models.FileField(null=True)

    def __str__(self):
        return self.categoryname


class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name



class orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey('signup', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('products',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
     
