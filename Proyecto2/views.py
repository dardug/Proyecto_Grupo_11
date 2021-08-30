
from django.shortcuts import render, redirect
from Usuarios.forms import usuario_form
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Usuarios.models import User
from Trivia.models import Pregunta
import random

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
        return redirect('principal')
    ctx={'form':usuario_form()}
    return render(request,template_name,ctx)






class Listar(LoginRequiredMixin,ListView):
	
	template_name="lista.html"
	model=User
	context_object_name= 'usuarios'

@login_required
def juego(request):
    if request.method == 'POST':
        print(request.POST)
        x=request.POST
        #print(x)
        #str(adad)
        
        preguntas=Pregunta.objects.all()
        print(preguntas)
             
        puntaje=0
        incorrecto=0
        correcto=0
        total=0          
        #str(dasda)
        for q in preguntas:
            total+=1
            #a=list()
            #s=append(q)
            y=q.respuesta_correcta
            z=request.POST.get(q.pregunta)
            w=q
            print(z)         
            print(y)
            print(q)

            #str(asa)
            if q.respuesta_correcta ==request.POST.get(q.pregunta):
                puntaje+=10
                correcto+=1

            else:
                incorrecto+=1
        str(asdfasd)
        porcentaje = (puntaje/(total*10))*100       
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







