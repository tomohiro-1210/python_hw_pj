from django.http import HttpResponse
from django.views.generic import TemplateView

def hwfunction(request):
    return HttpResponse('<o style="font-weight:bold;">Hello World！！</p>')

class hwClass(TemplateView):
    template_name = 'index.html'

class topPage(TemplateView):
    template_name = 'top.html'
    