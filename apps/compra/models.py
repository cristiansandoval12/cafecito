from django.db import models


    
class Proveedor(models.Model):
    nombre=models.CharField(max_length=1000)
    telefono=models.CharField( max_length=1000)
    direccion=models.CharField(max_length=1000)
    correo=models.CharField(max_length=1000)
    def __str__(self):
        return '{}'.format(self.nombre)
    

class Compra(models.Model):
    proveedor=models.ForeignKey(Proveedor, null=False, on_delete=models.CASCADE)
    id_compra=models.IntegerField()
    valor=models.IntegerField()
    cantidad=models.CharField( max_length=1000)
    fecha_compra=models.DateField()
    

    
