# from django.conf.urls import url, include
from django.urls import include, re_path, path
from apps.cmp.views import  ProductoView, ProductoNew , ProductoEdit, ProductoInactivar, VentasView, VentasEnc, VentasDet, ventas, VentaDetDelete
from .reportes import reporte_ventas, imprimir_venta

urlpatterns = [
    path(r'productos', ProductoView.as_view(), name='producto_list'),
    path(r'productos/new', ProductoNew.as_view(), name='producto_new'),
    path(r'productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path(r'productos/inactivar/<int:id>', ProductoInactivar, name='producto_inactivar'),
    # path(r'^eliminar/(?P<pk>\d+)/$', ProductosDelete.as_view(), name='Productos_eliminar'),
    path(r'ventas/list', reporte_ventas, name="ventas_print_all"),
    path(r'ventas/', VentasView.as_view(), name='ventas_list'),
    path(r'ventas/new', ventas, name='ventas_new'),
    path(r'ventas/edit/<int:venta_id>', ventas, name='ventas_edit'),
    path(r'ventas/<int:venta_id>/delete/<int:pk>', VentaDetDelete.as_view(), name='ventas_del'),
    path(r'ventas/<int:venta_id>/imprimir', imprimir_venta, name='ventas_print_one'),
]