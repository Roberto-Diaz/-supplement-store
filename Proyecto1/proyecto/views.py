from django.shortcuts import render
from proyecto.models import *


def getConsulta(request):
    rcliente = Cliente.objects.all()
    return render(request,'Consultar.html', {'regs':rcliente})

def index(request):
    return render(request, 'index.html')

def getCliente(request):
    return render(request, 'inserCliente.html')

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
    return render(request, 'inserCliente.html',{'res':'Cliente registrado correctamente'})
