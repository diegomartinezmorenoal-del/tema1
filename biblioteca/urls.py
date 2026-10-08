from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.lista_autores, name='lista_autores'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('socios/', views.lista_socios, name='lista_socios'),
]