from django.db import models

# Create your models here.
class Fabricante(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self) -> str:
        return self.nombre

class Remedio(models.Model):
    nombre=models.CharField(max_length=50)
    droga=models.CharField(max_length=20)
    vencimiento=models.DateField()
    def __str__(self) -> str:
        return self.nombre

class Farmaceutico(models.Model):
    nombre=models.CharField(max_length=50)
    num_vendidos=models.IntegerField()
    def __str__(self) -> str:
        return self.nombre 

