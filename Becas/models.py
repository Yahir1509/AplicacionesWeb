from django.db import models

# Create your models here.
from django.db import models

class Beca(models.Model):
    nombreBeca = models.CharField(max_length=255)
    tipoBeca = models.CharField(max_length=20)
    bActivo = models.BooleanField(null=True)

    def __str__(self):
        return self.nombreBeca
