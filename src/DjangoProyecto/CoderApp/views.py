from django.shortcuts import render
from django.http import HttpResponse

from CoderApp.models import ConductorVehiculo, Repuestos, Staff
from CoderApp.forms import VehiculoFormulario, ConductorBusqueda, RepuestosFormulario, StaffFormulario
from datetime import datetime


def vehiculo_formulario(request):

    if request.method == "POST":

        formulario = VehiculoFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data

            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            antiguedadvehiculo = datos.get("antiguedadvehiculo")
            modelovehiculo = datos.get("modelovehiculo")
            email = datos.get("email")

            vehiculo = ConductorVehiculo(nombre=nombre, apellido=apellido, antiguedadvehiculo=antiguedadvehiculo,modelovehiculo=modelovehiculo, email=email)

            vehiculo.save()

            return render(request, 'registrado.html')
    else:
        formulario = VehiculoFormulario()
    return render(request, "vehiculo_formulario.html", {"formulario":formulario})


def conductorbusqueda(request):

    formulario = ConductorBusqueda()
    return render(request, "conductor_busqueda.html", {"formulario":formulario})

def conductorbusquedarespuesta(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre")
        apellido = request.GET.get("apellido")

        if not nombre or not apellido:
            return HttpResponse("Datos incompletos")
            
        
        try:
            conductor_instance = ConductorVehiculo.objects.get(nombre__icontains=nombre, apellido__icontains=apellido)
            return render(request, "conductor_busqueda_respuesta.html", {"conductor":conductor_instance})
        except ConductorVehiculo.DoesNotExist:
            return HttpResponse("No se encontró el conductor")
    else:
        
        return HttpResponse("Método de solicitud no válido")
        

def repuestos(request):

    if request.method == "POST":
        formulario = RepuestosFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data

            repuestorequerido=datos.get("repuestorequerido")

            repuestos = Repuestos(repuestorequerido=repuestorequerido)

            repuestos.save()

            return HttpResponse("Su repuesto ha sido pedido")

    else:
        formulario=RepuestosFormulario()
    
    return render(request, "repuestos.html", {"formulario": formulario})



def staffregistro(request):
    if request.method == "POST":
        formulario = StaffFormulario(request.POST)
        if formulario.is_valid():
            datos_staff=formulario.cleaned_data
            
            nombre = datos_staff.get("nombre")
            apellido = datos_staff.get("apellido")
            email = datos_staff.get("email")
            creado = datetime.now()

            staff = Staff(nombre=nombre, apellido=apellido, email=email, creado=creado)

            staff.save()

            return HttpResponse(f"Funcionario {nombre} {apellido} correctamente registrado en el sistema.")
    
    else:
        formulario=StaffFormulario()
    
    return render(request, "staff_alta.html", {"formulario": formulario})

def index(request):
    return render(request, 'index.html')

def registrado(request):
    return render(request, 'registrado.html')