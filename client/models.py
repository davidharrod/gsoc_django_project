from django.db import models

# Create your models here.
class SysInfo(models.Model):
    username = models.CharField(max_length=200)
    os = models.CharField(max_length=50)
    compiler = models.CharField(max_length=30)
    cpu_architecture = models.CharField(max_length=20)


    