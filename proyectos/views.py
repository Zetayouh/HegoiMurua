from django.shortcuts import render, get_object_or_404
from .models import Proyecto
# Create your views here.

def selecciona_proyecto(request, proyecto_id):  
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    
    return render(request, 'proyectos/proyectos.html', {"proyecto":proyecto})