from django.shortcuts import render
from django.http import HttpResponse

from CoderApp.models import Sugerencias, Staff, StaffSolicitud, Avatar
from CoderApp.forms import UsuarioBusqueda, SugerenciasFormulario, StaffFormulario, UserRegistrationForm, UserEditForm, AvatarFormulario
from datetime import datetime

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from django.utils.decorators import method_decorator



def registrar(request):
    
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")

            form.save()

            return render(request, "index.html", {"mensaje": f"Se dio de alta el usuario {username}"})


    form = UserRegistrationForm()

    return render(request, "registro.html", {"form": form})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        
        formulario = UserEditForm(request.POST, instance=usuario)

        if formulario.is_valid():

            formulario.save()

            return render(request, "index.html")

    else:

        formulario = UserEditForm(instance = usuario)


        return render(request, "editar_perfil.html", {"formulario": formulario, "usuario": usuario})


def usuariobusqueda(request):

    formulario = UsuarioBusqueda()
    return render(request, "usuario_busqueda.html", {"formulario":formulario})

def usuariobusquedarespuesta(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre")
        apellido = request.GET.get("apellido")

        if not nombre or not apellido:
            return HttpResponse("Datos incompletos")
            
        try:
            usuario_instance = User.objects.get(first_name__icontains=nombre, last_name__icontains=apellido)
            return render(request, "usuario_busqueda_respuesta.html", {"usuario":usuario_instance})
        except User.DoesNotExist:
            return HttpResponse("No se encontró el usaurio")
    else:
        
        return HttpResponse("Método de solicitud no válido")
        

def sugerencias(request):

    if request.method == "POST":
        formulario = SugerenciasFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data

            sugerencia = datos.get("sugerencia")

            sugerencia = Sugerencias(sugerencia=sugerencia)

            sugerencia.save()

            return HttpResponse("Su sugerencia ha sido enviada y será evaluada. Muchas gracias!")

    else:
        formulario= SugerenciasFormulario()
    
    return render(request, "sugerencias.html", {"formulario": formulario})



def staffsolicitud(request):
    if request.method == "POST":
        formulario = StaffFormulario(request.POST)
        if formulario.is_valid():
            datos_staff=formulario.cleaned_data
            
            nombre = datos_staff.get("nombre")
            apellido = datos_staff.get("apellido")
            email = datos_staff.get("email")
            mensaje = datos_staff.get("mensaje")

            staff = StaffSolicitud(nombre=nombre, apellido=apellido, email=email, mensaje=mensaje)

            staff.save()

            return HttpResponse(f"{nombre} {apellido}, su solicitud ha sido enviada con éxito. En cuanto sea revisada, nos comunicaremos a su casilla de correo.")
    
    else:
        formulario=StaffFormulario()
    
    return render(request, "staff_solicitud.html", {"formulario": formulario})

def index(request):

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id).order_by('-created_at')
        if avatar:
            return render(request, 'index.html', {"url": avatar[0].image.url})

    return render(request, 'index.html')

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                avatar = Avatar.objects.filter(user=request.user.id).order_by('-created_at')     
                
                if avatar:
                    return render(request, "index.html", {"mensaje": f"Bienvenido a la plataforma!", "url": avatar[0].image.url})

                return render(request, "index.html", {"mensaje": f"Bienvenido {username}"})
            else:
                return render(request, "index.html", {"mensaje": f"Usuario o contraseña inválidos"})
            
        else:
            
            return render(request, "index.html", {"mensaje": "Datos incorrectos"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})





@method_decorator(staff_member_required, name='dispatch')
class StaffList(ListView):

    model = Staff
    template_name = 'staff_list.html'

@method_decorator(staff_member_required, name='dispatch')
class StaffDetalle(DetailView):
    model = Staff
    template_name = 'staff_detalle.html'

@method_decorator(staff_member_required, name='dispatch')
class StaffCreate(CreateView):

    model = Staff
    fields = ['nombre', 'apellido', 'email']
    template_name = 'staff_form.html'
    success_url = "/CoderApp/staff/list"

@method_decorator(staff_member_required, name='dispatch')
class StaffUpdate(UpdateView):

    model = Staff
    fields = ['nombre', 'apellido', 'email']
    template_name = 'staff_form.html'
    success_url = '/CoderApp/staff/list'

@method_decorator(staff_member_required, name='dispatch')
class StaffDelete(DeleteView):

    model = Staff
    template_name = "staff_confirm_delete.html"
    success_url = "/CoderApp/staff/list"

@method_decorator(staff_member_required, name='dispatch')
class SolicitudList(ListView):

    model = StaffSolicitud
    template_name = "solicitud_list.html"

@method_decorator(staff_member_required, name='dispatch')
class SolicitudDetalle(DetailView):

    model = StaffSolicitud
    template_name = "solicitud_detalle.html"

@method_decorator(staff_member_required, name='dispatch')
class SolicitudDelete(DeleteView):

    model = StaffSolicitud
    template_name = "solicitud_confirm_delete.html"
    success_url = "/CoderApp/solicitudes/list"


@login_required
def avatar(request):

    if request.method == "POST":
        
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            user = request.user
            avatar = Avatar(user=user, image=formulario.cleaned_data.get("image"))
            avatar.save()

            return render(request, 'index.html')


    formulario = AvatarFormulario()

    return render(request, "avatar.html", {"formulario": formulario})
    

def sobrenosotros(request):
    return render(request, 'sobrenosotros.html')
    