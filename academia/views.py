from django.shortcuts import render
from .models import Modalidade, Turma

def home(request):
    modalidades_ativas = Modalidade.objects.filter(ativa=True)
    return render(request, 'academia/home.html', {'modalidades': modalidades_ativas})


def grade_turmas(request):
    turmas = Turma.objects.select_related('modalidade').all()
    return render(request, 'academia/turmas.html', {'turmas': turmas})
