from dataclasses import dataclass
from mailbox import NoSuchMailboxError
from django.db import models
from django.forms import DateField

# Create your models here.
class Padre(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = DateField()

class Madre(models.Model):
    nombre= models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = DateField()
 