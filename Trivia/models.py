from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200,null=True)
    opción1 = models.CharField(max_length=200,null=True)
    opción2 = models.CharField(max_length=200,null=True)
    opción3 = models.CharField(max_length=200,null=True)
    opción4 = models.CharField(max_length=200,null=True)
    respuesta_correcta = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.pregunta)