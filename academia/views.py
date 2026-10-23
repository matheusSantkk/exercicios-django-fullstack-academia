from django.shortcuts import render
from .models import Modalidade, Turma

def home(request):
    modalidades_ativas = Modalidade.objects.filter(ativa=True)
    turmas = Turma.objects.all()
    
    context = {
        'modalidades': modalidades_ativas,
        'turmas': turmas
    }
    
    return render(request, 'academia/home.html', context)
