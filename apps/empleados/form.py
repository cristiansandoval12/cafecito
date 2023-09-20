from django import forms
from apps.empleados.models import empleados

class empleadosForm(forms.ModelForm):
    class Meta:
        model= empleados

        fields = [
            'nombre',
            'apellidos',
            'telefono',
            'estado',
        ]
        labels = {
            'nombre' : 'Nombre',
            'apellidos' : 'Apellidos',
            'telefono' : 'Telefono',
            'estado' : 'Estado',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
