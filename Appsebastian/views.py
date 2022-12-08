from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from Appsebastian.forms import *

# Create your views here.
def fabricante (request):
    fabricante_new=Fabricante(nombre="Bayer",email="bayer@bayer.com")
    fabricante_new.save()
    respuesta="Fabricante guardado"+fabricante_new.nombre
    return render(request,"Appsebastian/fabricante.html")
def fabricante (request):
    return render(request,"Appsebastian/fabricante.html")
def remedio (request):
    return render(request,"Appsebastian/remedio.html")
def farmaceutico (request):
    return render(request,"Appsebastian/farmaceutico.html")
    
#def formulariofarmaceutico (request):
 #   if request.method == "Post":
 #       var1=request.POST["nombre"]
 #       var2=request.POST["Numero"]
 #       formulario1=Farmaceutico(nombre=var1,numero=var2)
 #       formulario1.save()
 #   return render(request,"Appsebastian/inicio.html")
def formulariofarmaceutico (request):
    if request.method=="POST":
        formfarma=FarmaceuticoForm(request.POST)
              
        if formfarma.is_valid():
            informacion=formfarma.cleaned_data
            formulario1=Farmaceutico(nombre=informacion["nombre"], num_vendidos=informacion["num_vendidos"])
            formulario1.save()
            return render(request,"Appsebastian/inicio.html",{"mensaje":"Farmaceutico cargado correctamente."})
        else:
            formulario=FarmaceuticoForm()
        return render(request, "Appsebastian/formulariofarmaceutico.html", {"form":formulario})
    else:
        formulario=FarmaceuticoForm()
    return render(request, "Appsebastian/formulariofarmaceutico.html", {"form":formulario})

def formulariofabricante (request):
    if request.method=="POST":
        formfabri=FabricanteForm(request.POST)
              
        if formfabri.is_valid():
            informacion=formfabri.cleaned_data
            formulario1=Fabricante(nombre=informacion["nombre"], email=informacion["email"])
            formulario1.save()
            return render(request,"Appsebastian/inicio.html", {"mensaje":"Fabricante cargado correctamente."})
        else:
            formulario=FabricanteForm()
        return render(request, "Appsebastian/formulariofabricante.html", {"form":formulario})
    else:
        formulario=FabricanteForm()
    return render(request, "Appsebastian/formulariofabricante.html", {"form":formulario})
    
def formularioremedio (request):
    if request.method=="POST":
        formremedio=RemedioForm(request.POST)
              
        if formremedio.is_valid():
            informacion=formremedio.cleaned_data
            formulario1=Remedio(nombre=informacion["nombre"], droga=informacion["droga"], vencimiento=informacion["vencimiento"])
            formulario1.save()
            return render(request,"Appsebastian/inicio.html",{"mensaje":"Remedio cargado correctamente."})
        else:
            formulario=RemedioForm()
        return render(request, "Appsebastian/formularioremedio.html", {"form":formulario})
    else:
        formulario=RemedioForm()
    return render(request, "Appsebastian/formularioremedio.html", {"form":formulario})

def inicio (request):
    return render(request,"Appsebastian/inicio.html")

def busquedadroga(request):
    return render (request, "Appsebastian/busquedadroga.html")
    
def buscar(request):
    if request.GET["droga"]:
        droga= request.GET["droga"]
        nombre= Remedio.objects.filter(droga__icontains=droga)
        return render(request, "Appsebastian/resultadobusqueda.html", {"nombre":nombre, "droga":droga})
    else:
        respuesta= "No se enviaron datos"
    return HttpResponse(respuesta)