
from django.shortcuts import render, redirect
from Usuarios.forms import usuario_form
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Usuarios.models import User
from Trivia.models import Pregunta
import random
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages 

def inicio(request):
	template_name="inicio.html"
	ctx={}
	return render(request,template_name,ctx)

def login(request):
    template_name="login.html"
    if request.method=="POST":

        
        ctx={}
        return render(request,template_name,ctx)
        


def nuevo_usuario(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = usuario_form()
        if request.method=='POST':
            form = usuario_form(request.POST)
            if form.is_valid() :
                form.save()
                return redirect('login')
    ctx = {  
            'form':form  
        }  
    return render(request,"nuevo_usuario.html",ctx) 

class Listar(LoginRequiredMixin,ListView):
	
	template_name="lista.html"
	model=User
	context_object_name= 'usuarios'

@login_required
def juego(request):
    if request.method == 'POST':
        print(request.POST)
        x=request.POST

        
        preguntas=Pregunta.objects.all()
        print(preguntas)
             
        puntaje=0
        incorrecto=0
        correcto=0
        total=0          

        for q in preguntas:
            total+=1

            y=q.respuesta_correcta
            z=request.POST.get(q.pregunta)
            w=q
            print(z)         
            print(y)
            print(q)


            if q.respuesta_correcta ==request.POST.get(q.pregunta):
                puntaje+=10
                correcto+=1

            else:
                incorrecto+=1

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







