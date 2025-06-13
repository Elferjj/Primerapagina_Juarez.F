from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    calidad = models.CharField(max_length=30)
    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()    

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    seccion = models.CharField(max_length=30)

class Sucursales(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)