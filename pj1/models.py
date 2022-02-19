from statistics import mode
from django.db import models

# Create your models here.
class users(models.Model):
  username = models.CharField(max_length=50)
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  nname=models.CharField(max_length=50)
  sex = models.IntegerField()
  tell = models.CharField(max_length=13)
  email = models.EmailField()
  address = models.TextField()
  password = models.CharField(max_length=255)
  status_u = models.IntegerField(default=2)
  images = models.ImageField(upload_to='img_users',blank=True)
  
  
class Products(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField(default=0.0)
  qty = models.IntegerField(default=0)
  type = models.CharField(max_length=255)
  unit = models.CharField(max_length=50)
  productinsurance = models.IntegerField()
  brand = models.CharField(max_length=255)
  detail = models.TextField(blank=True)
  description = models.TextField(blank=True)
  img1 = models.ImageField(upload_to='img_produce',blank=True)
  img2 = models.ImageField(upload_to='img_produce',blank=True)
  img3 = models.ImageField(upload_to='img_produce',blank=True)
  