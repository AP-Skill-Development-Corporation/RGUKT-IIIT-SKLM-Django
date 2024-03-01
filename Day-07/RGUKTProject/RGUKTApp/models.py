from django.db import models

# Create your models here.

class Student(models.Model):
	stid = models.CharField(max_length=10)
	sname = models.CharField(max_length=50)
	sbranch = models.CharField(max_length=10,default="CSE")
	syear = models.IntegerField(default=1)