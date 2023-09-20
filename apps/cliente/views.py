from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.cliente.form import ClienteForm
from apps.cliente.form import Cliente
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json
# Create your views here.
def client(request):
    return render(request, 'venta/index.html')
    #return render(request, 'cliente/cliente_form.html')

def cliente_view(request):
    # if request.method =='POST':
    #     form = ClienteForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('Cliente:client')
    # else:
    #     form=ClienteForm()
    return render (request, 'cliente/cliente_form.html')

def cliente_list(request):
    cliente=Cliente.objects.all().order_by('id')
    contexto={'cliente':client}
    return render(request, 'cliente/cliente_list.html', contexto)

def ClienteEdit(request, id_cliente):
    cliente=Cliente.objects.get(id=id_cliente)
    if request.method=='GET':
        form=ClienteForm(instance=cliente)
    else:
        form=ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('cliente_listar')
    return render(request, 'cliente/cliente_form.html', {'form':form})

class ClienteList(ListView):
    model=Cliente
    template_name='cliente/cliente_list.html'
    context_object_name='obj'

class ClienteCreate(CreateView):
    model=Cliente
    form_class=ClienteForm
    template_name='cliente/cliente_form.html'
    context_object_name='obj'
    success_url=reverse_lazy('cliente_listar')

class ClienteUpdate(UpdateView):
    model=Cliente
    form_class=ClienteForm
    template_name='cliente/cliente_form.html'
    context_object_name='obj'
    success_url=reverse_lazy('cliente_listar')

class Clientedelete(DeleteView):
    model=Cliente
    template_name='cliente/cliente_delete.html'
    context_object_name='obj'
    success_url=reverse_lazy('cliente_listar')

def ClienteDelete(request, id_cliente):
    cliente=Cliente.objects.get(id=id_cliente)
    if request.method=='POST':
        ClienteDelete()
        return redirect('cliente_listar')
    return render(request, 'cliente/cliente_delete.html', {'cliente':client})

class ClienteList(ListView):
    model=Cliente
    template_name='cliente/cliente_list.html'
    context_object_name='obj'
    paginate_by= 4

def ClienteInactivar(request, id):
    template_name="cliente/cliente_inactivar.html"
    contexto={}
    prv=Cliente.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse("Cliente no existe" + str(id))
    
    if request.method=='GET':
        contexto={'obj': prv}
    
    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj': 'OK'}
        return HttpResponse("Cliente Inactivado")

    return render(request, template_name, contexto)