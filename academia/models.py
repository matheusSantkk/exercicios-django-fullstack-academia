from django.db import models
from django.core.exceptions import ValidationError

class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def delete(self, *args, **kwargs):
        if self.turma_set.exists():
            raise ValidationError("Não é possível excluir uma modalidade que possui turmas cadastradas.")
        super().delete(*args, **kwargs)


class Turma(models.Model):
    DIAS_SEMANA = [
        ('SEGUNDA', 'Segunda-feira'),
        ('TERCA', 'Terça-feira'),
        ('QUARTA', 'Quarta-feira'),
        ('QUINTA', 'Quinta-feira'),
        ('SEXTA', 'Sexta-feira'),
        ('SABADO', 'Sábado'),
    ]

    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    horario = models.TimeField()
    instrutor = models.CharField(max_length=100)
    vagas = models.PositiveIntegerField(default=10)

    class Meta:
        ordering = ['dia_semana', 'horario']

    def __str__(self):
        return f"{self.modalidade.nome} {self.get_dia_semana_display()} {self.horario.strftime('%H:%M')}"