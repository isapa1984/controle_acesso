from django.urls import path, include

from gestao_acesso.views import diversos, sistemas

urlpatterns = [
    path('', diversos.about, name='about'),
    path('sistemas/', sistemas.index, name='index'),
]