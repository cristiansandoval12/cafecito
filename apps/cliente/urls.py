from django.urls import include, re_path
from apps.cliente.views import client, ClienteEdit, ClienteList, ClienteCreate, ClienteDelete, ClienteUpdate, Clientedelete

urlpatterns = [
    re_path(r'^$', client, name='client'),
    re_path(r'^listar$', ClienteList.as_view(), name='cliente_listar'),
    re_path(r'^nuevo$', ClienteCreate.as_view(), name='cliente_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', ClienteUpdate.as_view(), name='cliente_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', Clientedelete.as_view(), name='cliente_eliminar'),
    re_path(r'^editar/(?P<id_cliente>\d+)/$', ClienteEdit, name='cliente_editar'),
    re_path(r'^eliminar/(?P<id_cliente>\d+)/$', ClienteDelete, name='cliente_eliminar'),
]
