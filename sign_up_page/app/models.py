from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    date = models.DateField(null=True)
    city = models.TextField()