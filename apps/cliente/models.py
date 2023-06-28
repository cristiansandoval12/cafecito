from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    direccion = models.TextField()
    
    def __str__(self):
        return'{} {}'.format(self.nombre,self.nombre)
    
