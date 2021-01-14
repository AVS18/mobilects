from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    semester = models.IntegerField()