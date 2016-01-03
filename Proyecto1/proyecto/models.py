from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    direccion = models.TextField()
    password = models.CharField(max_length=100)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    direccion = models.TextField()

class Sucursal(models.Model):
    ubicacion = models.TextField()


class Personal(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    direccion = models.TextField()
    edad = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal)

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.DecimalField(default=0.0, max_digits = 7, decimal_places = 2)
    proveedor = models.ForeignKey(Proveedor)
    personal = models.ForeignKey(Personal)

class Ventas(models.Model):
    total = models.DecimalField(max_digits = 7, decimal_places = 2)
    fecha = models.DateTimeField(auto_now_add = True)
    cliente = models.ForeignKey(Cliente)
    personal = models.ForeignKey(Personal)
    sucursal = models.ForeignKey(Sucursal)
