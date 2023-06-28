from django import forms
from apps.empleados.models import empleados

class empleadosForm(forms.ModelForm):
    class Meta:
        model= empleados

        fields = [
            'nombre',
            'apellidos',
            'telefono',
        ]
        labels = {
            'nombre' : 'Nombre',
            'apellidos' : 'Apellidos',
            'telefono' : 'Telefono',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
