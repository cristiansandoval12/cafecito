from django.db import models
from apps.cliente.models import Cliente
from apps.Productos.models import Productos
from apps.bases.models import ClassModelo

# Create your models here.
from django.db import models


class Venta(models.Model):
    cliente=models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    fecha_ventas=models.DateTimeField(auto_now_add=True)
    valor=models.IntegerField()
    cantidad=models.CharField(max_length=1000)

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)
