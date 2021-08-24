from django import forms

from Usuarios.models import User

class usuario_form(forms.ModelForm):
	class Meta:
		model=User
		fields= ["first_name","last_name","email","username","password"]





