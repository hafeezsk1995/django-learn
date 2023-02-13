from django.db import models
from .models import *
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    desc = models.CharField(max_length=50)
