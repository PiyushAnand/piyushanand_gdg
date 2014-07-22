from django.db import models

class Img(models.Model):
    image=models.CharField(max_length=500)

class About_us(models.Model):
    about_gdg=models.CharField(max_length=5000)
    about_gdj=models.CharField(max_length=5000)
    about_team=models.CharField(max_length=5000)

class About_img(models.Model):
    img=models.CharField(max_length=500)


# Create your models here.
