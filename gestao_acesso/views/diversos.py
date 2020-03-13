from django.shortcuts import render
from django.http import HttpResponse
from gestao_acesso.models import Sistema

# Create your views here.

def about(request):
    sistemas = Sistema.objects.all()
    str_list = ''.join(f'<li>{sistema.nome}</li>' for sistema in sistemas)
    return HttpResponse(f'Sistema de Gestão de Acessos<br><br>Lista de Sistemas <ul>{str_list}</ul>')


