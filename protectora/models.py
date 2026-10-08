from django.db import models
from django.contrib.auth.models import User

# 1. Modelo Protectora
class Protectora(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField()

    def __str__(self):
        return self.nombre

# 2. Modelo Colaborador
class Colaborador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_entrada_protectora = models.DateTimeField()

    def __str__(self):
        return self.nombre

# 3. Modelo Animal
class Animal(models.Model):
    cuidador = models.ForeignKey(User, on_delete=models.CASCADE) # Clave foránea al usuario de administración
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre