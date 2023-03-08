from django.db import models



class Impuesto(models.Model):
    descripcion = models.CharField(max_length=200)
    porcentaje = models.FloatField()


class Productos(models.Model):
    codigo_fabricante = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio_costo = models.FloatField()
    precio_venta= models.FloatField()
    existencia = models.IntegerField()
    cantidad_minima = models.IntegerField()
    cantidad_maxima = models.IntegerField()
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
