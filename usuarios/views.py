from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .forms import UsuarioForm

# Create your views here.
class UsuarioCreate(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    login_url = reverse_lazy('login')
    group_required = u'Administrador'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de usuário"
        context['botao'] = "Registrar"
        return context