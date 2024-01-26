from django.db import models
from django.contrib.auth.models import User


    
class Sugerencias(models.Model):
    sugerencia = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"Se ha sugerido la siguiente función : {self.sugerencia}"

class Staff(models.Model):

    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    creado=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido} -- {self.email}"

class StaffSolicitud(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    mensaje=models.CharField(max_length=300)

    def __str__(self):
        return f"Solicitud de {self.nombre}, {self.apellido}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

        




# Create your models here.
