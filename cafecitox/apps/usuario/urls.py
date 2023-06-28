from django.urls import include, re_path
from apps.usuario.views import RegistrarUsuario

urlpatterns = [
    re_path(r'^nuevo$', RegistrarUsuario.as_view(), name='Registrar'),
]
