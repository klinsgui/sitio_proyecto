from django.db import models
from django.utils import timezone

# Create your models here.
class Citar(models.Model):
    usuario = models.ForeignKey('auth.User')
    paciente = models.CharField(max_length=200)
    edad = models.IntegerField()
    tipo_cita = models.CharField(max_length=100)
    descripcion_malestar = models.TextField()
    fecha_reservacion = models.DateTimeField(default=timezone.now)
    fecha_cita = models.DateTimeField(blank=True, null=True)
    medico = models.CharField(max_length=200)
    realizada = models.BooleanField(default=False)

def publish(self):
    self.fecha_cita = timezone.now()
    self.save()

def __str__(self):
    return self.paciente
