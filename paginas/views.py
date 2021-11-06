from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#página inicial 
class IndexView(TemplateView):
    template_name = "modelo.html"

class SobreView(TemplateView):
    template_name = "sobre.html"