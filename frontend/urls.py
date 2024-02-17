from django.urls import path
from . import views

urlpatterns = [
    path('listar_tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('adicionar_tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    
]

