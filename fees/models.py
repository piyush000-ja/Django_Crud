from django.db import models


class Course(models.Model):
    Name = models.CharField(max_length=100)
    Course = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    Fees = models.IntegerField()


    def __str__(self):
        return self.Name
