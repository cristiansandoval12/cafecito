from django.urls import include, re_path
from apps.compra.views import index, compracreate,compralistar, compraeditar, compraborrar
urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^listar', compralistar.as_view(), name='compra_listar'),
    re_path(r'^nuevo$', compracreate.as_view(), name='compra_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', compraeditar.as_view(), name='compra_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', compraborrar.as_view(), name='compra_borrar'),
    
]
