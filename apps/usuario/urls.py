from django.urls import include, re_path
# from django.http import HttpResponse
from apps.usuario.views import RegistroUsuario

# def index(request):
#     return HttpResponse("usuario")

urlpatterns = [
    re_path(r'nuevo$', RegistroUsuario.as_view(), name='Registrar'),
]
