from django.shortcuts import render
from .models import Modalidade

def home(request):
    modalidades_ativas = Modalidade.objects.filter(ativa=True)
    
    context = {
        'modalidade': modalidades_ativas
    }
    
    return render(request, 'academia/home.html', context)
