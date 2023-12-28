from django.contrib import admin

from CoderApp.models import (
    ConductorVehiculo,
    Repuestos,
    Staff
)

admin.site.register(ConductorVehiculo)
admin.site.register(Repuestos)
admin.site.register(Staff)


# Register your models here.
