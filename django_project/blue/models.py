from django.db import models

# Create your models here.

class Blue(models.Model):
  
    title = models.CharField(
        max_length=80, blank=False, null=False)
    description = models.TextField()
    age = models.IntegerField(default=0)
