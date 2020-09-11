from django import forms
from gestao_acesso.models import Sistema

class SistemaForm(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'