from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from Appsebastian.forms import FarmaceuticoForm

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
    
#def formulariofarmaceutico (request):
 #   if request.method == "Post":
 #       var1=request.POST["nombre"]
 #       var2=request.POST["Numero"]
 #       formulario1=Farmaceutico(nombre=var1,numero=var2)
 #       formulario1.save()
 #   return render(request,"Appsebastian/inicio.html")
def formulariofarmaceutico (request):
    if request.method=="Post":
        form=FarmaceuticoForm(request.POST)
        print("----------------")
        print(form)
        print("----------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            var1=informacion["nombre"]
            var2=informacion["numero"]
            formulario1=Farmaceutico(nombre=var1,numero=var2)
            formulario1.save()
            return render(request,"Appsebastian/inicio.html")
        else:
            formulario=FarmaceuticoForm()
        return render(request, "Appsebastian/formulariofarmaceutico.html", {"form":formulario})
    else:
        formulario=FarmaceuticoForm()
    return render(request, "Appsebastian/formulariofarmaceutico.html", {"form":formulario})

def inicio (request):
    return render(request,"Appsebastian/inicio.html")    