from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_maxima = models.PositiveIntegerField()
    disponible = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre



class Reserva(models.Model):
    rut = models.CharField(max_length=12)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_termino = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.fecha_termino:
            self.fecha_termino = self.fecha_inicio + timedelta(hours=2)
        super().save(*args, **kwargs)