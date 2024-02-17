from django.shortcuts import render

import gerenciador_tarefas
from .models import Tarefa

from django.http import JsonResponse

def adicionar_tarefa(request):
    # Verifica se o token de autenticação está presente nos cabeçalhos da solicitação
    token = request.headers.get('Authorization')
    if gerenciador_tarefas.autenticador.verificar_token(token):
        # Se o token for válido, adicione a tarefa
        if request.method == 'POST':
            # Extrai os dados da solicitação POST
            dados = request.POST
            titulo = dados.get('titulo')
            descricao = dados.get('descricao')
            data_inicio = dados.get('data_inicio')
            data_conclusao_prevista = dados.get('data_conclusao_prevista')
            status = dados.get('status', 'Pendente')  # Status padrão é 'Pendente'

            # Crie uma nova instância de Tarefa com os dados fornecidos
            nova_tarefa = Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao,
                data_inicio=data_inicio,
                data_conclusao_prevista=data_conclusao_prevista,
                status=status
            )

            return JsonResponse({'mensagem': 'Tarefa adicionada com sucesso!'})

    return JsonResponse({'erro': 'Operação não autorizada. Token inválido.'}, status=401)


def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'listar_tarefas.html', {'tarefas': tarefas})
