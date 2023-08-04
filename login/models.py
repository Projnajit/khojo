from django.core.exceptions import DisallowedHost
from django.db import models
from django.db.models.base import Model

class users(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pasw = models.CharField(max_length=255)
    photo1 = models.ImageField(null=True,blank=True)