from django.contrib import admin

# Register your models here.
# -*- coding: utf8 -*-
from django.contrib import admin
from Trivia.models import Pregunta #Respuesta # Importamos todos los objetos de nuestra aplicación

# Register your models here.
admin.site.register(Pregunta) # Registramos el objeto Pregunta
#admin.site.register(Respuesta) # Registramos el objeto Respuesta

