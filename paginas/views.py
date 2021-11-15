from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#página inicial 
class IndexView(TemplateView):
    template_name = "paginas/index2.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"