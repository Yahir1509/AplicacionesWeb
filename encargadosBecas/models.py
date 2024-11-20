from django.db import models

# Create your models here.
from django.db import models

class encargadosBeca(models.Model):
    nombreEncargado = models.CharField(max_length=255)
    numeroTrabajador = models.CharField(max_length=20, unique=True)
    bActivo = models.BooleanField(null=True)

    def __str__(self):
        return self.nombreEncargado
