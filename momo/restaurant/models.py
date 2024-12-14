from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email = models.EmailField()
    message =models.TextField()
