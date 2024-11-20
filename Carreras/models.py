from django.db import models

# Create your models here.
from django.db import models

class Carrera(models.Model):
    cveCarrera = models.CharField(max_length=10, unique=True)
    nombreCarrera = models.CharField(max_length=255)
    areaCarrera = models.CharField(max_length=30)
    planEstudios = models.CharField(max_length=30)
    bActivo = models.BooleanField(null=True)

    def __str__(self):
        return self.nombreCarrera
