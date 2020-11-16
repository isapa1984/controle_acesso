from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from gestao_acesso.models import Sistema
from gestao_acesso.forms.sistemas import SistemaForm, BuscaSistemaForm

class SistemaListView(LoginRequiredMixin, ListView):
    template_name = "sistemas/index.html"
    context_object_name = 'sistemas'
    
    def get_queryset(self):
        queryset = Sistema.objects.all()
        
        form_busca = BuscaSistemaForm(self.request.GET)
        
        if form_busca['nome'].data:
            queryset = queryset.filter(nome__icontains=form_busca['nome'].data)

        if form_busca['sigla'].data:
            queryset = queryset.filter(sigla__icontains=form_busca['sigla'].data)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["titulo"] = 'Lista de Sistemas'
        context["form_busca"] = BuscaSistemaForm(self.request.GET)
        
        return context

# ------------------------------------

class SistemaCreateView(LoginRequiredMixin, CreateView):
    model = Sistema
    fields = '__all__'
    template_name = "sistemas/form.html"
    success_url = reverse_lazy('gestao_acesso:sistemas:index') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Cadastro de Sistema'
        return context

# ------------------------------------

class SistemaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sistema
    fields = '__all__'
    template_name = "sistemas/form.html"
    success_url = reverse_lazy('gestao_acesso:sistemas:index') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Edição de Sistema'
        return context

# ------------------------------------

class SistemaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sistema
    template_name = "sistemas/confirm_delete.html"
    success_url = reverse_lazy('gestao_acesso:sistemas:index') 