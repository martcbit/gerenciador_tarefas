import unittest
import sqlite3
import os
from datetime import datetime
from backend.gerenciador_tarefas import GerenciadorTarefasDB, Tarefa
from backend.autenticador import Autenticador

class TestGerenciadorTarefas(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.db_filename = 'test.db'
        self.autenticador = Autenticador()
        self.gerenciador_tarefas = GerenciadorTarefasDB(self.db_filename, self.autenticador)

    def tearDown(self):
        # Limpeza após os testes
        # Remover o banco de dados de teste
        if os.path.exists(self.db_filename):
            os.remove(self.db_filename)

    def test_adicionar_tarefa_autenticado(self):
        # Teste para verificar se uma tarefa pode ser adicionada por um usuário autenticado
        token = self.autenticador.gerar_token('usuario_teste')
        tarefa = Tarefa('Título', 'Descrição', datetime.now(), datetime.now())
        self.gerenciador_tarefas.adicionar_tarefa(tarefa, token)  # Fornecer o token como argumento
        tarefas = self.gerenciador_tarefas.listar_tarefas()
        self.assertTrue(len(tarefas) == 1)

    def test_adicionar_tarefa_nao_autenticado(self):
        # Teste para verificar se uma tarefa não pode ser adicionada por um usuário não autenticado
        tarefa = Tarefa('Título', 'Descrição', datetime.now(), datetime.now())
        self.gerenciador_tarefas.adicionar_tarefa(tarefa)  # Não fornecer token como argumento
        tarefas = self.gerenciador_tarefas.listar_tarefas()
        self.assertTrue(len(tarefas) == 0)

if __name__ == '__main__':
    unittest.main()
