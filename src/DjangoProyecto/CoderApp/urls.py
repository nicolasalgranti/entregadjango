from django.urls import path
from django.contrib.auth.views import LogoutView

from CoderApp.views import (
    usuariobusqueda,
    staffsolicitud,
    sugerencias,
    login_request,
    registrar,
    index,
    usuariobusquedarespuesta,
    StaffDelete,
    StaffDetalle,
    StaffUpdate,
    StaffList,
    StaffCreate,
    SolicitudDelete,
    SolicitudDetalle,
    SolicitudList,
    editar_perfil,
    avatar,
    sobrenosotros
)

urlpatterns = [
    path("usuariobusquedarespuesta/", usuariobusquedarespuesta, name="conductorbusquedarespuesta"),
    path("solicitudstaff/", staffsolicitud, name="staffsolicitud"),
    path("conductorbusqueda/", usuariobusqueda, name="conductorbusqueda"),
    path("sugerencias/", sugerencias, name="sugerencias"),
    path("login/", login_request, name="Login"),
    path("registrar", registrar, name="Registrar"),
    path("staff-eliminar/<pk>", StaffDelete.as_view(), name="Delete"),
    path("staff-detalle/<pk>", StaffDetalle.as_view(), name="Detail"),
    path("staff-editar/<pk>", StaffUpdate.as_view(), name="Edit"),
    path("staff-crear/", StaffCreate.as_view(), name="Create"),
    path("staff/list", StaffList.as_view(), name="List"),
    path("solicitud-eliminar/<pk>", SolicitudDelete.as_view(), name="soliDelete"),
    path("solicitud-detalle/<pk>", SolicitudDetalle.as_view(), name="soliDetalle"),
    path("solicitudes/list", SolicitudList.as_view(), name="soliList"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
    path("avatar", avatar, name = "avatar"),
    path("sobre-nosotros/", sobrenosotros, name = "sobrenosotros"),
    path("", index, name="index")
]
