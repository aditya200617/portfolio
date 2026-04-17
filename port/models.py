from django.db import models

# Create your models here.


class Port(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()