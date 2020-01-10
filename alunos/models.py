from django.db import models
from professores.models import Professor


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()

    generos = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Não Binário')
    )
    genero = models.CharField(max_length=3, choices=generos)
    nome_mae = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone_contato = models.CharField(max_length=13)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE)
        