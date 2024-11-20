from django.contrib import admin

# Register your models here.
# archivo: docentes/admin.py
from django.contrib import admin
from .models import Grupo

admin.site.register(Grupo)