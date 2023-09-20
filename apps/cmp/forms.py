from django import forms
from apps.cmp.models import Producto, VentasEnc, VentasDet

class ProductoForm(forms.ModelForm):

    class Meta:
        model=Producto

        fields = [
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

        exclude =[
            'um',
            'fm',
            'uc',
            'fc',
        ]

        widgets={
            'descripcion': forms.TextInput,
            # 'estado' : forms.CheckboxSelectMultiple, 
}

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['estado'] = forms.BooleanField()

class VentasEncForm(forms.ModelForm):
    fecha_venta = forms.DateField(widget=forms.DateInput())
    fecha_factura = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = VentasEnc
        fields = ['producto', 'fecha_venta', 'observacion', 'no_factura', 'fecha_factura', 'sub_total', 'descuento', 'total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['fecha_venta'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True


