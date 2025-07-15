from django import forms
from .models import Entrega

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ["codigo", "direccion", "estado", "repartidor", "latitud", "longitud"]
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "repartidor": forms.Select(attrs={"class": "form-select"}),
            "latitud": forms.NumberInput(attrs={"class": "form-control", "step": "0.000001"}),
            "longitud": forms.NumberInput(attrs={"class": "form-control", "step": "0.000001"}),
        }

    def clean_latitud(self):
        lat = self.cleaned_data.get("latitud")
        if lat is None or lat < -90 or lat > 90:
            raise forms.ValidationError("La latitud debe estar entre -90 y 90 grados.")
        return lat

    def clean_longitud(self):
        lon = self.cleaned_data.get("longitud")
        if lon is None or lon < -180 or lon > 180:
            raise forms.ValidationError("La longitud debe estar entre -180 y 180 grados.")
        return lon