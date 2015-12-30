from django.shortcuts import render
from proyecto.models import *


def getConsulta(request):
    rcliente = Cliente.objects.all()
    return render(request,'Consultar.html', {'regs':rcliente})

def index(request):
    return render(request, 'index.html')

def getCliente(request):
    return render(request, 'Cliente.html')

def postInsertarCliente(request):
    #id = request.POST['id']
    nom = request.POST['nom']
    apellidos = request.POST['apellidos']
    edad = request.POST['edad']
    sexo = request.POST['sexo']
    telefono = request.POST['telefono']
    email = request.POST['email']
    direccion = request.POST['direccion']
    password = request.POST['password']
    c = Cliente(nombre = nom, apellidos = apellidos,
    edad = edad, sexo = sexo, telefono = telefono, email = email,
    direccion = direccion, password = password)
    c.save()
    return render(request, 'Cliente.html',{'res':'Cliente registrado correctamente'})

def getProveedor(request):
    return render(request, 'Proveedor.html')

def postInsertarProveedor(request):
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    sexo = request.POST['sexo']
    telefono = request.POST['telefono']
    email = request.POST['email']
    direccion = request.POST['direccion']
    p = Proveedor(nombre = nombre, apellidos = apellidos, sexo = sexo,
    telefono = telefono, email = email, direccion = direccion)
    p.save()
    return render(request, 'Proveedor.html',{'res':'Proveedor registrado correctamente'})

def getSucursal(request):
    return render(request, 'Sucursal.html')

def postInsertarSucursal(request):
    ubi = request.POST['ubicacion']
    s = Sucursal(ubicacion = ubi)
    s.save()
    return render(request, 'Sucursal.html',{'res':'Sucursal registrada correctamente'})

def getPersonal(request):
    return render(request, 'Personal.html')

def postInsertarPersonal(request):
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    edad = request.POST['edad']
    sexo = request.POST['sexo']
    telefono = request.POST['telefono']
    email = request.POST['email']
    direccion = request.POST['direccion']
    sucursal = request.POST['sucursal']
    pe = Personal(nombre = nombre, apellidos = apellidos,
    edad = edad, sexo = sexo, telefono = telefono, email = email,
    direccion = direccion, sucursal_id = sucursal)
    pe.save()
    return render(request, 'Personal.html',{'res':'Personal registrado correctamente'})
