from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def galeria(request):
    template = loader.get_template('Galeria/galeria.html')
    return HttpResponse(template.render())