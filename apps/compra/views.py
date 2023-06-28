from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.compra.form import compraform
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.compra.models import Compra
# Create your views here.
#def index(request):
    #return render(request,'compra/index.html') 
def index(request):
    return render (request, 'compra/index.html')
# def compra_view(request):
#     if request.method()=='POST':  
#         form=compraform(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('compra:index')
#     else:
#         form=compraform()
#     return render(request,'compra/compra form.html',{'form':form})

class compracreate(CreateView):
    model= Compra
    form_class= compraform
    template_name='compra/compra_form.html'
    success_url=reverse_lazy('compra_listar')
    
    
class compralistar(ListView):
    model=Compra
    template_name='compra/compra_listar.html'
    paginate_by=2

class compraeditar(UpdateView):
    model=Compra
    form_class= compraform
    template_name='compra/compra_form.html'
    success_url= reverse_lazy('compra_listar')
    
class compraborrar(DeleteView):
    model=Compra
    template_name='compra/compra_borrar.html'
    success_url= reverse_lazy('compra_listar')