from django.contrib import admin
from django.urls import path
from alunos.views import *

urlpatterns = [
    path('deletar/aluno/<int:id>', deletar_aluno),
    path('atualizar/aluno/<int:id>', atualizar_aluno),
    path('aluno/<int:id>', detalhes_aluno),
    path('lista/alunos/', lista_alunos),
    path('cadastrar/alunos/', cadastrar_aluno),
    path('', home),
    path('admin/', admin.site.urls),
]
