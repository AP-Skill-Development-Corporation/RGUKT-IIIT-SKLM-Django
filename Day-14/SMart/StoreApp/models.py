from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	f = [
		('G',"Guest"),
		('C',"Client"),
		('M',"Manager")
	]
	simg = models.ImageField(upload_to='Profiles/')
	sage = models.IntegerField(default=20)
	srole = models.CharField(default='G',choices=f,max_length=6)