from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Programa

# Create your views here.

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programa.html')
    context = {
    'lista_programas': lista_programas,
    'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_programa(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    template = loader.get_template('detalle_programa.html')
    
    context = {
        'programa': programa,
    }
    
    return HttpResponse(template.render(context, request))