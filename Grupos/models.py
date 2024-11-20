from django.db import models

# Create your models here.
from django.db import models

class Grupo(models.Model):
    cveGrupo = models.CharField(max_length=10, unique=True)
    nombreGrupo = models.CharField(max_length=20)
    cuatrimestreGrupo = models.CharField(max_length=30)
    aulaNombre = models.CharField(max_length=30)
    aulaUbicacion = models.CharField(max_length=100)
    bActivo = models.BooleanField(null=True)

    def __str__(self):
        return self.nombreGrupo
