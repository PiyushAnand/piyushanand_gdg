from django.db import models

class Info_Form(models.Model):
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=5000)

class location(models.Model):
    map=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)

class contact(models.Model):
    social=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)

# Create your models here.
