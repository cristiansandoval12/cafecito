from django import forms
from apps.cliente.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'nombre',
            'apellido',
            'telefono',
            'direccion',
        ]
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellidos',
            'telefono':'Telefono',
            'direccion':'Direccion',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
        }