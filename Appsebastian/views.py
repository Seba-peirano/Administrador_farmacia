from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def fabricante (request):
    fabricante_new=Fabricante(nombre="Bayer",email="bayer@bayer.com")
    fabricante_new.save()
    respuesta="Fabricante guardado"+fabricante_new.nombre
    return HttpResponse(respuesta)
def fabricante (request):
    return render(request,"Appsebastian/fabricante.html")
def remedio (request):
    return render(request,"Appsebastian/remedio.html")
def farmaceutico (request):
    return render(request,"Appsebastian/farmaceutico.html")
    

def inicio (request):
    return render(request,"Appsebastian/inicio.html")    