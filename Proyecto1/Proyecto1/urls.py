from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proyecto1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^postinsertarsucursal', postInsertarSucursal),
    url(r'^inserSucursal/', getSucursal),
    url(r'^postinsertarproveedor', postInsertarProveedor),
    url(r'^inserProveedor/', getProveedor),
    url(r'^Consultar/', getConsulta),
    url(r'^postinsertarCliente/', postInsertarCliente),
    url(r'^inserCliente/', getCliente),
    url(r'^$',index),
    #url(r'^admin/', include(admin.site.urls)),

)
