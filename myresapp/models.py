from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)
    cover=models.ImageField(upload_to='images/')
    itemNo=models.IntegerField(null=True)
    rating=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    
    # def __str__(self):
    #     return self.title    