from django.urls import path
from Appsebastian import views
urlpatterns=[
path("", views.inicio, name="inicio"),
path("fabricante", views.fabricante, name="fabricante" ),
path("remedio", views.remedio, name="remedio" ),
path("farmaceutico", views.farmaceutico, name="farmaceutico" ),
path("formulariofarmaceutico", views.formulariofarmaceutico, name="formulariofarmaceutico" ),
]
