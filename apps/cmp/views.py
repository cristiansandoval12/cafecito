from django.shortcuts import render, redirect
from django.forms.models import BaseModelForm
from apps.venta.form import ventaform
from apps.venta.models import Venta
from apps.inv.models import Categoria
from apps.cmp.models import Producto, VentasEnc, VentasDet
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.cmp.forms import ProductoForm, VentasEncForm
from django.http import HttpResponse
import json
import datetime
from django.db.models import Sum
from .forms import VentasEncForm
from .models import Producto, VentasEnc, VentasDet
from django.utils import timezone
from xhtml2pdf import pisa
from django.template.loader import get_template
# Create your views here.
class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "cmp/producto_list.html"
    context_object_name = "obj"
    login_url = "login"

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "cmp/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("cmp:producto_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "cmp/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("cmp:producto_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)

def ProductoInactivar(request, id):
    template_name = "cmp/inactivar_prt.html"
    contexto = {}
    prt = Producto.objects.filter(pk=id).first()

    if not prt:
        return HttpResponse("Producto no existe" + str(id))

    if request.method == "GET":
        contexto = {"obj": prt}

    if request.method == "POST":
        prt.estado = False
        prt.save()
        contexto = {"obj": "OK"}
        return HttpResponse("Producto Inactivado")

    return render(request, template_name, contexto)

class VentasView(LoginRequiredMixin, generic.ListView):
    model = VentasEnc
    template_name = "cmp/ventas_list.html"
    context_object_name = "obj"
    login_url = "login"

def ventas(request, venta_id=None):
    template_name = "cmp/ventas.html"
    prod = Producto.objects.filter(estado=True)
    form_Ventas = {}
    contexto = {}

    if request.method == "GET":
        form_Ventas = VentasEncForm()
        enc = VentasEnc.objects.filter(pk=venta_id).first()

        if enc:
            det = VentasDet.objects.filter(venta=enc)
            fecha_venta = datetime.date.isoformat(enc.fecha_venta)
            fecha_factura = datetime.date.isoformat(enc.fecha_venta)
            e = {
                "fecha_venta": fecha_venta,
                "producto": enc.producto,
                "observacion": enc.observacion,
                "no_factura": enc.no_factura,
                "fecha_factura": fecha_factura,
                "sub_total": enc.sub_total,
                "descuento": enc.descuento,
                "total": enc.total,
            }
            form_Ventas = VentasEncForm(e)
        else:
            det = None

        contexto = {"productos": prod, "encabezado": enc, "detalle": det, "form_enc": form_Ventas}

    if request.method == "POST":
        fecha_venta = request.POST.get("fecha_venta")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        producto = request.POST.get("producto")
        sub_total = 0
        descuento = 0
        total = 0

        if not venta_id:
            prod = Producto.objects.get(pk=producto)
            enc = VentasEnc(
                fecha_venta=fecha_venta,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                producto=prod,
                uc=request.user,
            )
            if enc:
                enc.save()
                venta_id = enc.id
        else:
            enc = VentasEnc.objects.filter(pk=venta_id).first()
            if enc:
                enc.fecha_venta = fecha_venta
                enc.observacion = observacion
                enc.no_factura = no_factura
                enc.fecha_factura = fecha_factura
                enc.um = request.user.id
                enc.save()

        if not venta_id:
            return redirect("cmp:ventas_list")

        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        valor = request.POST.get("id_valor_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle = request.POST.get("id_descuento_detalle")
        total_detalle = request.POST.get("id_total_detalle")
        prod = Producto.objects.get(pk=producto)
        det = VentasDet(
            venta=enc,
            producto=prod,
            cantidad=cantidad,
            valor_prv=valor,
            descuento=descuento_detalle,
            costo=0,
            uc=request.user,
        )
        if det:
            det.save()
            sub_total = VentasDet.objects.filter(venta=venta_id).aggregate(Sum("sub_total"))
            descuento = VentasDet.objects.filter(venta=venta_id).aggregate(Sum("descuento"))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento = descuento["descuento__sum"]
            enc.save()

        return redirect("cmp:ventas_edit", venta_id=venta_id)

    return render(request, template_name, contexto)

class VentaDetDelete(LoginRequiredMixin, generic.DeleteView):
    model = VentasDet
    template_name = "cmp/ventas_det_del.html"
    context_object_name = "obj"

    def get_success_url(self):
        venta_id = self.kwargs["venta_id"]
        return reverse_lazy("cmp:ventas_edit", kwargs={"venta_id": venta_id})

class VentasView(LoginRequiredMixin, generic.ListView):
    model=VentasEnc
    template_name="cmp/ventas_list.html"
    context_object_name="obj"
    login_url="login"

def ventas(request, venta_id=None):
    template_name = "cmp/ventas.html"
    prod = Producto.objects.filter(estado=True)
    form_Ventas = {}
    contexto = {}
    
    if request.method == 'GET':
        form_Ventas = VentasEncForm()
        enc = VentasEnc.objects.filter(pk=venta_id).first()
        
        if enc:
            det = VentasDet.objects.filter(venta=enc)
            fecha_venta = datetime.date.isoformat(enc.fecha_venta)
            fecha_factura = datetime.date.isoformat(enc.fecha_venta)
            e = {
                'fecha_venta': fecha_venta,
                'producto': enc.producto,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }
            form_Ventas = VentasEncForm(e)
        else:
            det = None
        
        contexto = {'productos': prod, 'encabezado': enc, 'detalle': det, 'form_enc': form_Ventas}
    
    if request.method == 'POST':
        fecha_venta = request.POST.get("fecha_venta")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        producto = request.POST.get("producto")
        sub_total = 0
        descuento = 0
        total = 0
        
        if not venta_id:
            prod = Producto.objects.get(pk=producto)
            enc = VentasEnc(
                fecha_venta=fecha_venta,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                producto=prod,
                uc=request.user
            )
            if enc:
                enc.save()
                venta_id = enc.id
        else:
            enc = VentasEnc.objects.filter(pk=venta_id).first()
            if enc:
                enc.fecha_venta = fecha_venta
                enc.observacion = observacion
                enc.no_factura = no_factura
                enc.fecha_factura = fecha_factura
                enc.um = request.user.id
                enc.save()
        
        if not venta_id:
            return redirect("cmp:ventas_list")
        
        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        valor = request.POST.get("id_valor_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle = request.POST.get("id_descuento_detalle")
        total_detalle = request.POST.get("id_total_detalle")
        prod = Producto.objects.get(pk=producto)
        det = VentasDet(
            venta=enc,
            producto=prod,
            cantidad=cantidad,
            valor_prv=valor,
            descuento=descuento_detalle,
            costo=0,
            uc=request.user
        )
        if det:
            det.save()
            sub_total = VentasDet.objects.filter(venta=venta_id).aggregate(Sum('sub_total'))
            descuento = VentasDet.objects.filter(venta=venta_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento = descuento["descuento__sum"]
            enc.save()
        
        return redirect("cmp:ventas_edit", venta_id=venta_id)
    
    return render(request, template_name, contexto)

# class VentaDetDelete(LoginRequiredMixin, generic.DeleteView):
#     model = VentasDet
#     template_name = "cmp/ventas_det_del.html"
#     context_object_name = "obj"
    
#     def get_success_url(self):
#         venta_id = self.kwargs['venta_id']
#         return reverse_lazy('cmp:ventas_edit', kwargs={'venta_id': venta_id})

