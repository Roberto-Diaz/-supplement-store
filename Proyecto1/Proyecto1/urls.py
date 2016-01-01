from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proyecto1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^postinsertarventas/', postInsertarVentas),
    url(r'^Ventas/', getVentas),
    url(r'^postinsertarproductos/', postInsertarProductos),
    url(r'^Productos/', getProductos),
    url(r'^postinsertarpersonal/', postInsertarPersonal),
    url(r'^Personal/', getPersonal),
    url(r'^postinsertarsucursal', postInsertarSucursal),
    url(r'^Sucursal/', getSucursal),
    url(r'^postinsertarproveedor', postInsertarProveedor),
    url(r'^Proveedor/', getProveedor),
    url(r'^Consultar/', getConsulta),
    url(r'^postinsertarCliente/', postInsertarCliente),
    url(r'^Cliente/', getCliente),
    url(r'^$',index),
    #url(r'^admin/', include(admin.site.urls)),

)
