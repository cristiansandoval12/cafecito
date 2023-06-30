# from django.conf.urls import url, include
from django.urls import include, re_path
from apps.Productos.views import  index, ProductosCreate , ProductosList, ProductosEdit, ProductosDelete


urlpatterns = [
    re_path(r'$', index, name='index'),
    re_path(r'^listar', ProductosList.as_view(), name='Productos_listar'),
    re_path(r'^nuevo$', ProductosCreate.as_view(), name='Productos_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', ProductosEdit.as_view(), name='Productos_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', ProductosDelete.as_view(), name='Productos_eliminar'),
]
