from django.db import models

# Create your models here.
class Admin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length = 50)
    
    def __str__(self):
        return self.email
class User(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length = 50)
    
    def __str__(self):
        return self.email

class Registration(models.Model):
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=20,)
    image=models.ImageField(upload_to = 'image/')
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    bloodgrp=models.CharField(max_length=50)
    specialisation=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone=models.IntegerField()
    session=models.DateField()
    rollno=models.IntegerField()
    address=models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email

    

