from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from gestao_acesso.models import Perfil, Sistema
from gestao_acesso.forms.perfis import PerfilForm

class PerfilListView(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = "perfis/index.html"
    context_object_name = 'perfis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Lista de Perfis'
        return context
    

# ------------------------------------

class PerfilCreateView(LoginRequiredMixin, CreateView):
    model = Perfil
    fields = '__all__'
    template_name = "perfis/form.html"
    success_url = reverse_lazy('gestao_acesso:perfis:index') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Cadastro de Perfil'
        context['sistemas'] = Sistema.objects.all()
        return context

# ------------------------------------

class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfil
    fields = '__all__'
    template_name = "perfis/form.html"
    success_url = reverse_lazy('gestao_acesso:perfis:index') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Edição de Perfil'
        context['sistemas'] = Sistema.objects.all()
        return context

# ------------------------------------

class PerfilDeleteView(LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = "perfis/confirm_delete.html"
    success_url = reverse_lazy('gestao_acesso:perfis:index') 