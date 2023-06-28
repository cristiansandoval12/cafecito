from django.db import models

# Create your models here.
class empleados(models.Model):
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    telefono=models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.nombre,self.nombre )
