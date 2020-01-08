from django.shortcuts import render
from alunos.forms import AlunoForm
from alunos.models import Aluno


def home(request):
    return render(request, 'base.html')

def cadastrar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        args = {
            'form':form,
            'msg':'O cadastro foi realizado com sucesso'
        }
        return render(request, 'cadastro.html', args)
    args = {'form':form}
    return render(request, 'cadastro.html', args)

def lista_alunos(request):
    lista_alunos = Aluno.objects.filter().all()

    args = {'lista_alunos':lista_alunos}
    return render(request, 'listadealunos.html', args)

def detalhes_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)

    args = {'aluno':aluno}
    return render(request, 'detalhes.html', args)

def atualizar_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    
    args = {'form':form}
    
    if form.is_valid():
        form.save()
        args = {
            'msg':'Cadastro atulizado com sucesso'
        }
    return render(request, 'atualizaraluno.html', args)

def deletar_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()

    args = {
        'msg':'O aluno foi deletado com sucesso',
        'aluno':aluno
        }
    return render(request, 'detalhes.html', args)