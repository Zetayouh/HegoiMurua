from django.shortcuts import render

from proyectos.models import Proyecto
from .models import Aptitud, Categoria

# Create your views here.

def home(request):
    proyectos=Proyecto.objects.all()
    aptitudes=Aptitud.objects.all()
    categorias=Categoria.objects.all()
    return render(request, "WebApp/home.html", {"proyectos": proyectos, "aptitudes":aptitudes, "categorias":categorias})

