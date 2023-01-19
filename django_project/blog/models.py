
from pyexpat import model
from re import M
from unicodedata import name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Deleviry(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class MyModel(models.Model):
  
    title = models.CharField(
        max_length=80, blank=False, null=False)
    description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    age = models.IntegerField(default=0)

    def fun_check(self):
        return self.title


class M1(models.Model):
    address = models.TextField()
    name = models.CharField(max_length=100, blank=True, null=True)


class M2(models.Model):
    job =  models.CharField(
        max_length=80, blank=False, null=False)
    title = models.CharField(
        max_length=80, blank=False, null=False)     
    name = models.CharField(max_length=100, blank=True, null=True)    



class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

class Phone(models.Model):
    number = models.CharField(max_length=100, blank=True, null=True)
    customer = models.OneToOneField(Customer,related_name='no',on_delete=models.CASCADE
    )

class Interest(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)


class Person(models.Model):
    name = models.CharField(max_length=220, blank=True, null=True)
    interest  = models.ManyToManyField(Interest, blank=True, null=True
    )
