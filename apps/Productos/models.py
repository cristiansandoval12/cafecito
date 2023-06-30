from django.db import models

# Create your models here.
class Productos(models.Model):
    Cantidad_Productos=models.IntegerField()
    Valor=models.IntegerField()
    Descripcion=models.CharField(max_length=70)

    def _str_(self):
        return '{} {}'.format(self.Cantidad_Productos,self.Cantidad_Productos)
