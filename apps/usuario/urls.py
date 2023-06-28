from django.urls import include, re_path
from apps.usuario.views import RegistroUsuario

urlpatterns = [
        re_path(r'^nuevo$', RegistroUsuario.as_view(), name='Registrar'),
]
