from django.urls import path

from CoderApp.views import (
    conductorbusqueda,
    staffregistro,
    vehiculo_formulario,
    repuestos,
    index,
    conductorbusquedarespuesta,
    registrado
)

urlpatterns = [
    path("conductorbusquedarespuesta/", conductorbusquedarespuesta, name="conductorbusquedarespuesta"),
    path("registrostaff/", staffregistro, name="staffregistro"),
    path("conductorbusqueda/", conductorbusqueda, name="conductorbusqueda"),
    path("registro/", vehiculo_formulario, name="vehiculo_formulario"),
    path("repuestos/", repuestos, name="repuestos"),
    path("registrado/", registrado, name="registrado"),
    path("", index, name="index")
]
