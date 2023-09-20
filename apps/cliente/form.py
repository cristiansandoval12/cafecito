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
            'estado',
        ]
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellidos',
            'telefono':'Telefono',
            'direccion':'Direccion',
            'estado':'Estado',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }