from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    direccion = models.TextField()
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return'{} {}'.format(self.nombre,self.apellido)
    
