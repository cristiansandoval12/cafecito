from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.form import registroform

class registrarusuario(CreateView):
    model= User
    template_name='usuario/registrar.html'
    form_class= registroform
    success_url = reverse_lazy('compra_listar')


# Create your views here.
