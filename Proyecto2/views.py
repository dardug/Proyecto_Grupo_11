
from django.shortcuts import render
from Usuarios.forms import usuario_form
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Usuarios.models import User
from Trivia.models import Pregunta

def inicio(request):
	template_name="inicio.html"
	ctx={}
	return render(request,template_name,ctx)

def login(request):
	template_name="login.html"
	ctx={}
	return render(request,template_name,ctx)

def nuevo_usuario(request):
	template_name="nuevo_usuario.html"
	if request.method=='POST':
		first_name=request.POST.get("first_name",None)
		last_name=request.POST.get("last_name",None)
		email=request.POST.get("email",None)
		
		username=request.POST.get("username",None)
		password=request.POST.get("password",None)
		
		a=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password)

	ctx={'form':usuario_form()}
	return render(request,template_name,ctx)



class Listar(LoginRequiredMixin,ListView):
	
	template_name="lista.html"
	model=User
	context_object_name= 'usuarios'


def juego(request):
    if request.method == 'POST':
        print(request.POST)
        preguntas=Pregunta.objects.all()
        puntaje=0
        incorrecto=0
        correcto=0
        total=0
        for q in preguntas:
            total+=1
            print(request.POST.get(q.pregunta))
            print(q.respuesta_correcta)
            print()
            if q.respuesta_correcta ==  request.POST.get(q.pregunta):
                puntaje+=10
                correcto+=1
            else:
                incorrecto+=1
        porcentaje = puntaje/(total*10) *100
        context = {
            'puntaje':puntaje,
            'time': request.POST.get('timer'),
            'correcto':correcto,
            'incorrecto':incorrecto,
            'porcentaje':porcentaje,
            'total':total
        }
        return render(request,'resultados.html',context)
    else:
        preguntas=Pregunta.objects.all()
        context = {
            'preguntas':preguntas
        }
        return render(request,'preguntas.html',context)







