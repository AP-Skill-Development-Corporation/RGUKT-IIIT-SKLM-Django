from django.db import models

# Create your models here.

class Employee(models.Model):
	op = [
		('0','-- Select your Designation --'),
		('1','Intern'),
		('2','Junior Trainee'),
		('3','Junior Developer'),
		('4','Senior Trainee'),
	]
	epid = models.CharField(max_length=15)
	ename = models.CharField(max_length=50)
	edesg = models.CharField(max_length=5,choices=op,default='0')
	esal = models.IntegerField(default=12000)