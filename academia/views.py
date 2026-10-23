from django.shortcuts import render, redirect
from .models import Modalidade, Turma
from .forms import AlunoForm

def home(request):
    modalidades_ativas = Modalidade.objects.filter(ativa=True)
    turmas = Turma.objects.all()

    form = AlunoForm()
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'modalidades': modalidades_ativas,
        'turmas': turmas,
        'form': form,
    }
    
    return render(request, 'academia/home.html', context)
