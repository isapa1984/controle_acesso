from django import forms
from gestao_acesso.models import Sistema

class SistemaForm(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'


class BuscaSistemaForm(forms.Form):
    """
    Formulário de busca
    """
    nome = forms.CharField(label='Nome do Sistema', required=False)
    sigla = forms.CharField(label='Sigla', required=False)