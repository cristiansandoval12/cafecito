from django import forms
from apps.Productos.models import Productos


class Productosform(forms.ModelForm):
    class Meta:
        model=Productos

        fields =[
            'nombre',
            'cantidad_productos',
            'valor',
            'descripcion',
            'estado',
        ]
        labels={
            'nombre':'Nombre',
            'cantidad_productos': 'Cantidad de productos',
            'valor': 'Valor del producto',
            'descripcion': 'Descripcion',
            'estado': 'Estado',
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_productos': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }