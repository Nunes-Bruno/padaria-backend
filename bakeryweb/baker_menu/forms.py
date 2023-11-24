from django import forms
from django.core.validators import RegexValidator

class MeuFormulario(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    # telefone = forms.CharField(max_length=15, validators=[RegexValidator(r'^\+?55?\s?\(?[1-9]{2}\)?\s?9?[0-9]{4}-?[0-9]{4}$', message="Número de celular inválido. O formato aceito é: '999999999'.")])
