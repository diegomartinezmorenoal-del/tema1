from django.shortcuts import render
from .models import Autor, Libro, Socio

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/lista_autores.html', {'autores': autores})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'biblioteca/lista_socios.html', {'socios': socios})