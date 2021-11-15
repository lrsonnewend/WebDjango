from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from braces.views import GroupRequiredMixin
from .forms import UsuarioForm
from .models import Perfil

# Create your views here.
class UsuarioCreate(LoginRequiredMixin,CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de usuário"
        context['botao'] = "Registrar"
        return context


    def form_valid(self, form):
        if(User.objects.filter(groups_name="Docente").exists()):
            grupo = get_object_or_404(Group, name = 'Docente')
            self.object.group.add(grupo)
        else:
            self.object.groups.add(form.cleaned_data['grupo'])

        url = super().form_valid(form)
        
        self.object.save()

        Perfil.objects.create(usuario=self.object)
        return url

class PerfilUpdate(UpdateView):
    model = Perfil
    template_name='cadastros/form.html'
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('index2')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Meus dados"
        context['botao']= "Atualizar"
        return context