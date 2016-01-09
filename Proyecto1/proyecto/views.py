from django.shortcuts import render
from proyecto.models import *


def getConsulta(request):
    rcliente = Cliente.objects.all()
    return render(request,'Consultar.html', {'regs':rcliente})

def index(request):
    return render(request, 'index.html')

#def productosLineas(request):
#    return render(request, 'productosLineas.html')
def eliminarCliente(request):
	c = Cliente(request.POST['id'])
	c.delete()
	return getConsulta(request)



def productosLin(request):
    return render(request, 'productosLineas.html')

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
    return getConsulta(request)
    #return render(request, 'Consultar.html',{'res':'Cliente registrado correctamente'})

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


def getProductos(request):
    return render(request, 'Productos.html')

def postInsertarProductos(request):
    nombre = request.POST['nombre']
    marca = request.POST['marca']
    precio = request.POST['precio']
    proveedor = request.POST['proveedor']
    personal = request.POST['personal']

    pr = Productos(nombre = nombre, marca = marca,
    precio = precio, proveedor_id = proveedor, personal_id = personal)
    pr.save()
    return render(request, 'Productos.html',{'res':'Producto registrado correctamente'})

def getVentas(request):
    return render(request, 'Ventas.html')

def postInsertarVentas(request):
    total = request.POST['total']
    cliente = request.POST['cliente']
    personal = request.POST['personal']
    sucursal = request.POST['sucursal']

    v= Ventas(total = total, cliente_id = cliente, personal_id = personal, sucursal_id = sucursal)
    v.save()
    return render(request, 'Ventas.html',{'res':'Venta registrada correctamente'})



def buscar(request):
    if 'id' in request.GET:
        id = request.GET['id']
        c = Cliente.objects.get(id)
        return render(request, 'Consultar.html',{'res':p})
    return render(request, 'Consultar.html')

def postModificar(request):
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
    return getConsulta(request)
