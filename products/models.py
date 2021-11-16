from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length= 50)
    price = models.IntegerField()
     

class salelog(models.Model):
    book   = models.ForeignKey('salelog', on_delete= models.CASCADE)
    date   = models.DateField()
    name   = models.CharField(max_length= 50)
    cancel = models.BooleanField()