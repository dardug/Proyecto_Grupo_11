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

"""
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2

    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )
        return user      


	class Meta:
		model=User
		fields= ["first_name","last_name"]
"""




