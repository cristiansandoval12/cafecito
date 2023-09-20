from django import forms
from apps.venta.models import Venta, Cliente
class ventaform(forms.ModelForm):
    cliente=forms.ModelChoiceField(
        queryset=Cliente.objects.filter(estado=True)
        .order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model= Venta
        
        fields =[
            'valor',
            'cantidad',
            'cliente',
        ]

        labels={
            'valor':'Valor',
            'cantidad':'Cantidad',
            'cliente':'Cliente',
        }

        widgets={
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'cliente': forms.Select(attrs={'class':'form-control'}),
        }



