from django.http import HttpResponse
from django.template import loader


def pasieka(request):
    template = loader.get_template('Pasieka/main.html')
    return HttpResponse(template.render())
    
