from django.db import models


class ConductorVehiculo(models.Model):
    
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30, null=True)
    antiguedadvehiculo=models.IntegerField(null=True)
    modelovehiculo=models.CharField(max_length=20, null=True)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido} -- {self.email} -- {self.modelovehiculo}"
    
class Repuestos(models.Model):
    repuestorequerido = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"Se ha pedido el repuesto : {self.repuestorequerido}"

class Staff(models.Model):

    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    creado=models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido} -- {self.email}"
        
    




# Create your models here.
