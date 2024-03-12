from django.db import models

# Create your models here.
class Courses(models.Model):
    coursename = models.CharField(max_length=50,unique=True)
    courseFee = models.IntegerField()
    courseDuration = models.CharField(max_length=50)



class Signup(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)












