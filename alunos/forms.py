from django import forms
from alunos.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'