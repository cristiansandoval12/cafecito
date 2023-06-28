from django.shortcuts import render, redirect
from django.http import HttpResponse
#from apps.empleados.models import empleados
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# , UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.empleados.form import empleadosForm
from apps.empleados.form import empleados
# Create your views here.
def index(request):
    return render (request, 'empleados/index.html')
    #  return render(request, 'empleados/empleados_form.html')
# def empleados_view(request):
#     if request.method =='POST':
#         form = empleadosForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('empleados:index')
#         return render(request, 'empleados/empleados_list.html')
#     else:
#         form=empleadosForm()
#     return render (request, 'empleados/empleados_form.html',{'form':form})

class empleadosList(ListView):
    model=empleados
    template_name='empleados/empleados_list.html'

class empleadosCreate(CreateView):
    model=empleados
    form_class=empleadosForm
    template_name='empleados/empleados_form.html'
    success_url=reverse_lazy('empleados_listar')

# def empleados_list(request):
#     Empleados=empleados.objects.all().order_by('id')
#     contexto={'Empleados':index}
#     return render(request, 'empleados/empleados_list.html', contexto)

# def empleados_edit(request, id_empleados):
#     Empleados=empleados.objects.get(id=id_empleados)
#     if request.method=='GET':
#         form=empleadosForm(instance=empleados)
#     else:
#         form=empleadosForm(request.POST, instance=empleados)
#         if form.is_valid():
#             form.save()
#         return redirect('empleados_listar')
# #        return render(request, 'empleados/empleados_list.html')
#     return render(request, 'empleados/empleados_form.html', {'form':form})

class EmpleadosUpdate (UpdateView):
    model = empleados
    form_class=empleadosForm
    template_name='empleados/empleados_form.html'
    success_url=reverse_lazy('empleados_listar')

class empleadosdelete(DeleteView):
    model=empleados
    template_name='empleados/empleados_delete.html'
    success_url=reverse_lazy('empleados_listar')

# def empleados_view(request):
#     return render (request, 'empleados/empleados_form.html')


# def EmpleadosEdit(request, id_empleados):
#     Empleados=empleados.objects.get(id=id_empleados)
#     if request.method=='GET':
#         form=empleadosForm(instance=empleados)
#     else:
#         form=empleadosForm(request.POST, instance=empleados)
#         if form.is_valid():
#             form.save()
#         # return redirect('empleados_listar')
#         return render(request, 'empleados/empleados_list.html')
#     return render(request, 'empleados/empleados_form.html', {'form':form})

# def EmpleadosDelete(request, id_empleados):
#     Empleados=empleados.objects.get(id=id_empleados)
#     if request.method=='POST':
#         EmpleadosDelete()
#         return redirect('empleados_listar')
#     return render(request, 'empleados/empleados_delete.html', {'empleados':index})

# class SolicitudUpdate(UpdateView):
#     model=Solicitud
#     second_model=Persona
#     template_name='adopcion/solicitud_form.html'
#     form_class=SolicitudForm
#     second_form_class=PersonaForm
#     succes_url=reverse_lazy('solicitud_listar')

class empleadosList(ListView):
    model=empleados
    template_name='empleados/empleados_list.html'
    paginate_by=3
