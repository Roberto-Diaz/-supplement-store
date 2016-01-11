from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

from proyecto import views
from proyecto.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proyecto1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^postModificar/', postModificar),
    url(r'^postModificarProveedor/', postModificarProveedor),
    url(r'^postModificarSucursal/', postModificarSucursal),
    url(r'^postModificarPersonal/', postModificarPersonal),
    url(r'^postModificarProducto/', postModificarProducto),
    url(r'^postModificarVenta/', postModificarVenta),
    url(r'^buscarCliente/', buscar),
    url(r'^buscarProveedor/', buscarProveedor),
    url(r'^buscarSucursal/', buscarSucursal),
    url(r'^buscarPersonal/', buscarPersonal),
    url(r'^buscarProducto/', buscarProducto),
    url(r'^buscarVenta/', buscarVenta),
    url(r'^postinsertarventas/', postInsertarVentas),
    url(r'^Ventas/', getVentas),
    url(r'^postinsertarproductos/', postInsertarProductos),
    url(r'^Productos/', getProductos),
    url(r'^postInsertarPersonal/', postInsertarPersonal),
    url(r'^Personal/', getPersonal2),
    url(r'^postinsertarsucursal', postInsertarSucursal),
    url(r'^Sucursal/', getSucursal),
    url(r'^postinsertarproveedor', postInsertarProveedor),
    url(r'^Proveedor/', getProveedor),
    url(r'^Consultar/', getConsulta),
    url(r'^postinsertarCliente/', postInsertarCliente),
    url(r'^Cliente/', getCliente),
    url(r'^productosLineas/',productosLin),
    url(r'^postEliminar/',eliminarCliente),
    url(r'^postEliminarProve/',eliminarProveedor),
    url(r'^postEliminarSucu/',eliminarSucursal),
    url(r'^postEliminarPersonal/',eliminarPersonal),
    url(r'^postEliminarProducto/',eliminarProducto),
    url(r'^postEliminarVenta/',eliminarVenta),
    #url(r'^',productosLineas),
    #url(r'^$',views.index, name="factura"),
    url(r'^$',index),
    #url(r'^$',views.index, name='inde),
    #url(r'^admin/', include(admin.site.urls)),

)
