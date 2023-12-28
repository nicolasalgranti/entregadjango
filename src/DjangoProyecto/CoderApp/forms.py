from django import forms

class VehiculoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    apellido = forms.CharField(max_length=20, required=False)
    antiguedadvehiculo = forms.IntegerField()
    modelovehiculo = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()

class ConductorBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    apellido = forms.CharField(max_length=20, required=False)

class StaffFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    apellido = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()

class RepuestosFormulario(forms.Form):
    repuestorequerido=forms.CharField(max_length=20, required=False)
