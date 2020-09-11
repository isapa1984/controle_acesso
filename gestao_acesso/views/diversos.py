from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from gestao_acesso.models import Sistema


# Create your views here.

class AboutView(TemplateView):
    template_name = "diversos/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sistemas"] = Sistema.objects.all()
        return context
    
