from django import forms
from apps.compra.models import Compra
class compraform(forms.ModelForm):
    class Meta:
        model= Compra
        
        fields =[
            'id_compra',
            'valor',
            'cantidad',
            'fecha_compra',
            'proveedor',
        ]

        labels={
            'id_compra':'Id_compra',
            'valor':'Valor',
            'cantidad':'Cantidad',
            'fecha_compra':'Fecha_compra',
            'proveedor':'Proveedores',
        }

        widgets={
            'id_compra': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_compra': forms.TextInput(attrs={'class':'form-control'}),
            'proveedor': forms.Select(attrs={'class':'form-control'}),
        }



