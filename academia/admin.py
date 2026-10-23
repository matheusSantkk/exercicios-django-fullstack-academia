from django.contrib import admin
from .models import Modalidade, Turma, Aluno

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativa')
    list_filter = ('ativa', )
    search_fields = ('nome', )
    
@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('modalidade', 'dia_semana', 'horario', 'instrutor', 'vagas')
    list_filter = ('modalidade', 'dia_semana')
    search_fields = ('instrutor', )

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')
    filter_horizontal = ('turmas', )
