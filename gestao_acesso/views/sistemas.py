from django.shortcuts import render
from gestao_acesso.models import Sistema

# Create your views here.

def index(request):
    sistemas = Sistema.objects.order_by('nome')
    context = {
        'sistemas': sistemas
    }
    return render(request, 'sistemas/index.html', context)