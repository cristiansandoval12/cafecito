from django.urls import include, re_path
from apps.usuario.views import registrarusuario

urlpatterns = [
     re_path(r'^nuevo$', registrarusuario.as_view(), name='registrar'),
]
