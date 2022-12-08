from django.urls import path
from Appsebastian.views import *
urlpatterns=[
path("", inicio, name="inicio"),
path("fabricante", fabricante, name="fabricante" ),
path("remedio", remedio, name="remedio" ),
path("farmaceutico", farmaceutico, name="farmaceutico" ),
path("formulariofarmaceutico", formulariofarmaceutico, name="formulariofarmaceutico" ),
path("formulariofabricante", formulariofabricante, name="formulariofabricante" ),
path("formularioremedio", formularioremedio, name="formularioremedio" ),
path("busquedadroga", busquedadroga, name="busquedadroga" ),
path("buscar/", buscar, name="buscar" ),
]
