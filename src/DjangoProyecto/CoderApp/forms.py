from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UsuarioBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    apellido = forms.CharField(max_length=20, required=False)

class StaffFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    apellido = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))

class SugerenciasFormulario(forms.Form):
    sugerencia=forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}), required=False, label="Deje una sugerencia")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget = forms.PasswordInput)
    # vehiculo = forms.CharField(label = "Modelo del vehículo")
    # antiguedadvehiculo = forms.CharField(label = "Año del modelo")


    class Meta:
        model = User
        fields = ["username","first_name", "last_name",  "email", "password1", "password2"]

class UserEditForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

class AvatarFormulario(forms.Form):
    image = forms.ImageField()
    