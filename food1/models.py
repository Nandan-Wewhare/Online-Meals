from django.db import models

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=30)
    add = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    ordername = models.CharField(max_length=20)
    quantity = models.IntegerField()
