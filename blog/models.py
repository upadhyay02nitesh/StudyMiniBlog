from email.mime import image
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    # url1=models.URLField()
    # url2=models.URLField()
    # url3=models.URLField()
    # url4=models.URLField()
    
class Study(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    url1=models.URLField()
    url2=models.URLField()
    url3=models.URLField()
    url4=models.URLField()
    image=models.ImageField()
