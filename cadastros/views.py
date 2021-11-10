from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import Campo, Atividade

# Create your views here.
class CampoCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

#UPDATE
class CampoUpdate(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeUpdate(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


#DELETE
class CampoDelete(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Campo
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeDelete(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Atividade
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')


#LISTAR
class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'
    


class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'