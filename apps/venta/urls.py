from django.urls import include, re_path, path
from apps.venta.views import index, ventacreate,ventalistar,ventaeditar, ventaborrar, VentaInactivar
from django.contrib.auth.decorators import login_required
# from .reportes import reporte_ventas

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^listar', login_required(ventalistar.as_view()), name='venta_listar'),
    re_path(r'^nuevo$', ventacreate.as_view(), name='venta_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', ventaeditar.as_view(), name='venta_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', ventaborrar.as_view(), name='venta_borrar'),
    path(r'inactivar/<int:id>', VentaInactivar, name='venta_inactivar'),
    # path(r'ventas/listado', reporte_ventas, name='ventas_print_all'),
]
