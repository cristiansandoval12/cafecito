from django.db import models
from apps.bases.models import ClassModelo
from django.core.validators import MinValueValidator
# from apps.cmp.models import Producto

# Create your models here.
class Producto(ClassModelo):
    nombre= models.CharField(max_length=50, default='')
    cantidad_productos=models.IntegerField(validators=[MinValueValidator(0)])
    valor=models.IntegerField(validators=[MinValueValidator(0)])
    descripcion=models.CharField(max_length=70)
    estado=models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.Cantidad_Productos,self.Cantidad_Productos)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion=self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural="Productos"

class VentasEnc(ClassModelo):
    fecha_venta = models.DateField(null=True, blank=True)
    observacion = models.TextField(blank=True, null=True)
    no_factura = models.CharField(max_length=100)
    fecha_factura = models.DateField(null=True, blank=True)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        self.total = self.sub_total - self.descuento
        super(VentasEnc, self).save()

    class Meta:
        verbose_name_plural = "Encabezado Ventas"
        verbose_name = "Encabezado Venta"

class VentasDet(ClassModelo):
    venta = models.ForeignKey(VentasEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    valor_prv = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)
    
    def save(self):
        self.sub_total = float(int(self.cantidad)) * float(self.valor_prv)
        self.total = self.sub_total - float(self.descuento)
        super(VentasDet, self).save()

    class Meta:
        verbose_name_plural = "Detalles Ventas"
        verbose_name = "Detalle Venta"

