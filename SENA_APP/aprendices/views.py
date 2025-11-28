from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz


def aprendices(request):
    lista_aprendices= Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    context={
    'lista_aprendices': lista_aprendices,
}
    return HttpResponse(template.render(context, request))
    


def home(request):
    return render(request, 'main.html')
context={
    
}