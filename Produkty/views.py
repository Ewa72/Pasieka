from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Miody
from django.views import generic

def miody(request):
     mymiody = Miody.objects.all()#Miody.objects.all().values()
     #template = loader.get_template('Produkty/miody_list.html')
     template = loader.get_template('Produkty/miody.html')
     context = {
         'mymiody': mymiody,
         }
     return HttpResponse(template.render(context, request))

def miod_details(request, id):
  mymiod = Miody.objects.get(id=id)
  template = loader.get_template('Produkty/miod_details.html')
  #template = loader.get_template('Produkty/Pomoc.html')
  context = {
    'mymiod': mymiod,
  }
  return HttpResponse(template.render(context, request))


class MiodyListView(generic.ListView):
    model = Miody
 
 
