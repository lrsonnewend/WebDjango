from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from braces.views import GroupRequiredMixin
from .forms import UsuarioForm

# Create your views here.
class UsuarioCreate(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    #group_required = u'Administrador'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de usuário"
        context['botao'] = "Registrar"
        return context

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name = 'Docente')
        url = super().form_valid(form)
        self.object.group.add(grupo)
        self.object.save()
        return url