from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'telefone', 'data_nascimento', 'turmas']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'seu@email.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '(00) 00000-0000'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'turmas': forms.CheckboxSelectMultiple(attrs={'class': 'form-checkboxes'}),
        }