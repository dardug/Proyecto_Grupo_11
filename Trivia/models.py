from django.db import models

# Create your models here.

class Pregunta(models.Model):
	pregunta = models.CharField(max_length=200) # Campo tipo Char con un máximo de 200 caracteres de longitud.
	fecha_publicacion = models.DateTimeField('fecha de publicacion', auto_now=True) # Campo de tipo Fecha y Hora y que se asigne automáticamente el tiempo
	def __str__(self):

		return self.pregunta # La clase retornará el campo que queramos especificar, en este caso, la pregunta


class Respuesta(models.Model):
	pregunta = models.ForeignKey("Pregunta",on_delete=models.CASCADE) # Campo con que se relaciona la pregunta de esta respuesta.
	opcion = models.CharField(max_length=200) # Campo tipo Char con un máximo de 200 caracteres de longitud.
	votes = models.IntegerField(default=0) # Campo entero que por defecto empezará en 0.
	def __str__(self):
		return self.opcion # La clase retornará el campo que queramos especificar, en este caso, la opción