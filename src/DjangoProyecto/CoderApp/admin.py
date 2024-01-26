from django.contrib import admin


from CoderApp.models import (
    Sugerencias,
    Staff,
    StaffSolicitud,
    Avatar
)

admin.site.register(Sugerencias)
admin.site.register(Staff)
admin.site.register(StaffSolicitud)
admin.site.register(Avatar)

# Register your models here.
