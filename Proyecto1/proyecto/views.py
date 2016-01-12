from django.shortcuts import render
from django.http import HttpResponse
from proyecto.models import *

def handler404(request):
    return render(request,'error/error404.html')

def handler400(request):
    return render(request,'error/error400.html')

def handler403(request):
    return render(request,'error/error403.html')

def handler500(request):
    return render(request,'error/error500.html')


def getCliente(request):
    rcliente = Cliente.objects.all()
    return render(request,'Cliente.html', {'regs':rcliente})



def index(request):
    return render(request, 'index.html')

def acerca(request):
    return render(request, 'acerca-de.html')

#def productosLineas(request):
#    return render(request, 'productosLineas.html')
def eliminarCliente(request):
	c = Cliente(request.POST['id'])
	c.delete()
	return getCliente(request)


def eliminarProveedor(request):
	c = Proveedor(request.POST['id'])
	c.delete()
	return getProveedor(request)


def eliminarPersonal(request):
	c = Personal(request.POST['id'])
	c.delete()
	return getPersonal2(request)

def eliminarProducto(request):
	c = Productos(request.POST['id'])
	c.delete()
	return getProductos(request)

def eliminarSucursal(request):
	c = Sucursal(request.POST['id'])
	c.delete()
	return getSucursal(request)

def eliminarVenta(request):
	c = Ventas(request.POST['id'])
	c.delete()
	return getVentas(request)



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
    return getCliente(request)
    #return render(request, 'Consultar.html',{'res':'Cliente registrado correctamente'})

def getProveedor(request):
    rprovedor = Proveedor.objects.all()
    return render(request,'Proveedor.html', {'regs':rprovedor})


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
    return getProveedor(request)
    #return render(request, 'Proveedor.html',{'res':'Proveedor registrado correctamente'})

def getSucursal(request):
    rsucursal = Sucursal.objects.all()
    return render(request,'Sucursal.html', {'regs':rsucursal})

def postInsertarSucursal(request):
    ubi = request.POST['ubicacion']
    s = Sucursal(ubicacion = ubi)
    s.save()
    return getSucursal(request)
    #return render(request, 'Sucursal.html',{'res':'Sucursal registrada correctamente'})

#def getPersonal(request):
#    return render(request, 'Personal.html')
def getPersonal2(request):
    rpersonal = Personal.objects.all()
    suc = Sucursal.objects.all()
    return render(request,'Personal.html', {'regs':rpersonal, 'r':suc})

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
    return getPersonal2(request)
    #return render(request, 'Personal.html',{'res':'Personal registrado correctamente'})




#def getProductos(request):
#    return render(request, 'Productos.html')

def getProductos(request):
    rproductos = Productos.objects.all()
    per = Personal.objects.all()
    pro = Proveedor.objects.all()
    return render(request,'Productos.html', {'regs':rproductos, 'per':per, 'pro':pro})

def postInsertarProductos(request):
    nombre = request.POST['nombre']
    marca = request.POST['marca']
    precio = request.POST['precio']
    proveedor = request.POST['proveedor']
    personal = request.POST['personal']
    pr = Productos(nombre = nombre, marca = marca,
    precio = precio, proveedor_id = proveedor, personal_id = personal)
    pr.save()
    return getProductos(request)


def getVentas(request):
    rventas = Ventas.objects.all()
    cli = Cliente.objects.all()
    per = Personal.objects.all()
    suc= Sucursal.objects.all()
    return render(request,'Ventas.html', {'regs':rventas, 'cli':cli, 'per':per, 'suc':suc})

def postInsertarVentas(request):
    total = request.POST['total']
    cliente = request.POST['cliente']
    personal = request.POST['personal']
    sucursal = request.POST['sucursal']

    v= Ventas(total = total, cliente_id = cliente, personal_id = personal, sucursal_id = sucursal)
    v.save()
    return getVentas(request)
    #return render(request, 'Ventas.html',{'res':'Venta registrada correctamente'})



def buscar(request):
    if 'idbus' in request.GET:
        id = request.GET['idbus']
        c = Cliente.objects.get(id=id)
        return render(request, 'ModificarCliente.html',{'res':c})
    return render(request, 'ModificarCliente.html')

def buscarProveedor(request):
    if 'idbus' in request.GET:
        id = request.GET['idbus']
        c = Proveedor.objects.get(id=id)
        return render(request, 'ModificarProveedor.html',{'res':c})
    return render(request, 'ModificarProveedor.html')

def buscarVenta(request):
    if 'idbus' in request.GET:
        id = request.GET['idbus']
        c = Ventas.objects.get(id=id)
        return render(request, 'ModificarVenta.html',{'res':c})
    return render(request, 'ModificarVenta.html')

def buscarSucursal(request):
    if 'idbus' in request.GET:
        id = request.GET['idbus']
        c = Sucursal.objects.get(id=id)
        return render(request, 'ModificarSucursal.html',{'res':c})
    return render(request, 'ModificarSucursal.html')

def buscarPersonal(request):
    if 'idbus' in request.GET:
        id = request.GET['idbus']
        p = Personal.objects.get(id=id)
        return render(request, 'ModificarPersonal.html',{'res':p})
    return render(request, 'ModificarPersonal.html')

def buscarProducto(request):
    if 'idbus' in request.GET:
        id = request.GET['idbus']
        p = Productos.objects.get(id=id)
        return render(request, 'ModificarProducto.html',{'res':p})
    return render(request, 'ModificarProducto.html')

def postModificar(request):
    id = request.POST['id']
    nom = request.POST['nom']
    apellidos = request.POST['apellidos']
    edad = request.POST['edad']
    sexo = request.POST['sexo']
    telefono = request.POST['telefono']
    email = request.POST['email']
    direccion = request.POST['direccion']
    password = request.POST['password']
    c = Cliente(id= id, nombre = nom, apellidos = apellidos,
    edad = edad, sexo = sexo, telefono = telefono, email = email,
    direccion = direccion, password = password)
    c.save()
    return getCliente(request)


def postModificarProveedor(request):
        id = request.POST['id']
        nom = request.POST['nom']
        apellidos = request.POST['apellidos']
        sexo = request.POST['sexo']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        c = Proveedor(id= id, nombre = nom, apellidos = apellidos,
         sexo = sexo, telefono = telefono, email = email,
        direccion = direccion)
        c.save()
        return getProveedor(request)

def postModificarPersonal(request):
        id = request.POST['id']
        nom = request.POST['nom']
        apellidos = request.POST['apellidos']
        sexo = request.POST['sexo']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        edad = request.POST['edad']
        sucursal_id = request.POST['sucursal_id']
        p = Personal(id= id, nombre = nom, apellidos = apellidos,
         sexo = sexo, telefono = telefono, email = email,
        direccion = direccion,edad=edad,sucursal_id=sucursal_id)
        p.save()
        return getPersonal2(request)


def postModificarVenta(request):
        id = request.POST['id']
        total = request.POST['total']
        fecha = request.POST['fecha']
        cliente_id = request.POST['cliente_id']
        personal_id = request.POST['personal_id']
        sucursal_id = request.POST['sucursal_id']
        p = Ventas(id= id, total = total, fecha= fecha,
        cliente_id= cliente_id, personal_id = personal_id, sucursal_id=sucursal_id)
        p.save()
        return getVentas(request)

def postModificarProducto(request):
        id = request.POST['id']
        nom = request.POST['nom']
        marca = request.POST['marca']
        precio = request.POST['precio']
        proveedor_id = request.POST['proveedor_id']
        personal_id = request.POST['personal_id']
        p = Productos(id= id, nombre = nom, marca = marca,
         precio = precio, proveedor_id = proveedor_id, personal_id = personal_id)
        p.save()
        return getProductos(request)

def postModificarSucursal(request):
        id = request.POST['id']
        ubicacion = request.POST['ubicacion']
        c = Sucursal(id = id, ubicacion = ubicacion)
        c.save()
        return getSucursal(request)
