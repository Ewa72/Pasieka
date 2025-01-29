from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Miody
from django.views.generic.detail import DetailView

def miody(request):
    mymiody = Miody.objects.all()#Miody.objects.all().values()
    template = loader.get_template('Produkty/miody.html')
    context = {
        'mymiody': mymiody,
        }
    return HttpResponse(template.render(context, request))

class MiodyDetailView(DetailView):
    model = Miody