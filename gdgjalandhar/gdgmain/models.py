from django.db import models

class menu(models.Model):
    menu_title = models.CharField(max_length=1000)
    menu_subtitle = models.CharField(max_length=5000)
    href=models.CharField(max_length=500)

class banner(models.Model):
    banner1 = models.CharField(max_length=500)

class social(models.Model):
    logo = models.CharField(max_length=500)
    facebook = models.CharField(max_length=500)
    google = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    social1 = models.CharField(max_length=500)
# Create your models here.
