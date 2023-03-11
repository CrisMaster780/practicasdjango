from django.db import models
from django.contrib.auth.models import User



class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    direccion= models.CharField(max_length=200)
    telefono= models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

