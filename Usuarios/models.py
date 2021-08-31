from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	
	fecha_nacimiento=models.DateField(null=True, blank=True)
	direccion=models.CharField(max_length=255, null=True, blank=True)
	telefono=models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		db_table="usuarios"













	







