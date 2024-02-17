import uuid
import json
from datetime import datetime
import sqlite3

class Tarefa:
    def __init__(self, titulo, descricao, data_inicio, data_conclusao_prevista, status="Pendente"):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_conclusao_prevista = data_conclusao_prevista
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data_inicio": self.data_inicio.strftime("%Y-%m-%d %H:%M:%S"),
            "data_conclusao_prevista": self.data_conclusao_prevista.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status
        }

class GerenciadorTarefasDB:
    def __init__(self, db_filename, autenticador):
        self.db_filename = db_filename
        self.autenticador = autenticador  # Adicionando autenticador como atributo
        self.conn = sqlite3.connect(db_filename)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS tarefas
                     (id TEXT PRIMARY KEY,
                      titulo TEXT,
                      descricao TEXT,
                      data_inicio TEXT,
                      data_conclusao_prevista TEXT,
                      status TEXT)''')
        self.conn.commit()

    def adicionar_tarefa(self, tarefa):
        # Token de autenticação
        token = input("Digite seu token de autenticação: ")
        if self.verificar_token(token):
            self.c.execute('''INSERT INTO tarefas VALUES (?, ?, ?, ?, ?, ?)''',
                           (tarefa.id, tarefa.titulo, tarefa.descricao,
                            tarefa.data_inicio.strftime("%Y-%m-%d %H:%M:%S"),
                            tarefa.data_conclusao_prevista.strftime("%Y-%m-%d %H:%M:%S"),
                            tarefa.status))
            self.conn.commit()
        else:
            print("Token inválido. Operação não autorizada.")

    def verificar_token(self, token):
        return self.autenticador.verificar_token(token)

    def editar_tarefa(self, tarefa_id, novo_titulo, nova_descricao, nova_data_inicio, nova_data_conclusao_prevista, novo_status):
        self.c.execute('''UPDATE tarefas SET titulo=?, descricao=?, data_inicio=?, data_conclusao_prevista=?, status=? WHERE id=?''',
                       (novo_titulo, nova_descricao, nova_data_inicio.strftime("%Y-%m-%d %H:%M:%S"),
                        nova_data_conclusao_prevista.strftime("%Y-%m-%d %H:%M:%S"), novo_status, tarefa_id))
        self.conn.commit()

    def remover_tarefa(self, tarefa_id):
        self.c.execute('''DELETE FROM tarefas WHERE id=?''', (tarefa_id,))
        self.conn.commit()

    def listar_tarefas(self):
        self.c.execute('''SELECT * FROM tarefas''')
        return self.c.fetchall()

    def listar_tarefas_ordenadas(self, criterio):
        if criterio in ['titulo', 'descricao', 'data_inicio', 'data_conclusao_prevista', 'status']:
            self.c.execute('''SELECT * FROM tarefas ORDER BY {}'''.format(criterio))
            return self.c.fetchall()
        else:
            raise ValueError("Critério de ordenação inválido.")

    def filtrar_tarefas(self, criterio, valor):
        if criterio in ['titulo', 'descricao', 'data_inicio', 'data_conclusao_prevista', 'status']:
            self.c.execute('''SELECT * FROM tarefas WHERE {} = ?'''.format(criterio), (valor,))
            return self.c.fetchall()
        else:
            raise ValueError("Critério de filtragem inválido.")