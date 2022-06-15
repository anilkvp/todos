"""
todos models

"""
from django.db import models

# Create your models here.


class Item(models.Model):
    """
    Item class
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
