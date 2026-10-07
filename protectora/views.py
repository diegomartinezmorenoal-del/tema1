from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'protectora/lista_animales.html', {'animales': animales})

def lista_protectoras(request):
    protectoras = Protectora.objects.all()
    return render(request, 'protectora/lista_protectoras.html', {'protectoras': protectoras})

def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'protectora/lista_colaboradores.html', {'colaboradores': colaboradores})