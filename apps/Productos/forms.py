from django import forms
from apps.Productos.models import Productos


class Productosform(forms.ModelForm):
    class Meta:
        model=Productos

        fields =[
            'Cantidad_Productos',
            'Valor',
            'Descripcion',
        ]
        labels={
            'Cantidad_Productos': 'Cantidada de productos',
            'Valor': 'Valor del producto',
            'Descripcion': 'Descripcion',
        }
        Widgets={
            'Cantidad_Productos': forms.TextInput(attrs={'class':'form-control'}),
            'Valor': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }