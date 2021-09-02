from django import forms
from django.contrib.auth.models import AbstractUser

from Usuarios.models import User

from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  

class usuario_form(UserCreationForm):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')  
    email = forms.EmailField()  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ["username"]	





