from django.db import models

# Create your models here.

class user_master(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class contact_master(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    mobile = models.BigIntegerField(default=0)
    message = models.CharField(max_length=250)

class feedback_master(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    mobile = models.BigIntegerField(default=0)
    message = models.CharField(max_length=250)
