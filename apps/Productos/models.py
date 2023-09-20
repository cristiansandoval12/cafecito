from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Productos(models.Model):
    nombre= models.CharField(max_length=50, default='')
    cantidad_productos=models.IntegerField(validators=[MinValueValidator(0)])
    valor=models.IntegerField(validators=[MinValueValidator(0)])
    descripcion=models.CharField(max_length=70)
    estado=models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.Cantidad_Productos,self.Cantidad_Productos)

