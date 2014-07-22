from django.db import models

class event(models.Model):
    img=models.CharField(max_length=1000)
    img_logo=models.CharField(max_length=1000)
    location=models.CharField(max_length=1000)
    status=models.CharField(max_length=5000)
    event_title=models.CharField(max_length=3000)
    event_desc=models.CharField(max_length=10000)

# Create your models here.
