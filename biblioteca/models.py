from django.db import models

# 1. Modelo Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

# 2. Modelo Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    paginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# 3. Modelo Socio
class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_alta = models.DateTimeField()

    def __str__(self):
        return self.nombre