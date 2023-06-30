from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class meta:
        model= User
        fields=[
            'nombreusuario',
            'primer_nombre',
            'apellido',
            'email',
        ]
        labels={
            'nombreusuario':'Nombre de usuario',
            'primer_nombre':'Nombre',
            'apellido':'Apellidos',
            'email':'Correo',
        }
        # Widgets={
        #     'nombreusuario': User.TextInput(attrs={'class':'form-control'}),
        #     'primer_nombre': User.TextInput(attrs={'class':'form-control'}),
        #     'apellido': User.TextInput(attrs={'class':'form-control'}),
        #     'email':User.TextInput(attrs={'class':'form-control'}),
        #     }