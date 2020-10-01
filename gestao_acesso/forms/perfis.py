from django import forms
from gestao_acesso.models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'