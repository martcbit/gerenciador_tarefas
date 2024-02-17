import sqlite3
import uuid
import hashlib

class Autenticador:
    def __init__(self):
        self.tokens = {}

    def gerar_token(self, usuario):
        token = str(uuid.uuid4())
        self.tokens[token] = usuario
        return token

    def verificar_token(self, token):
        return token in self.tokens

    def gerar_hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

class GerenciadorTarefasDB:
    def __init__(self, db_filename, autenticador):
        self.db_filename = db_filename
        self.autenticador = autenticador
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

    def adicionar_tarefa(self, tarefa, token):
        if self.autenticador.verificar_token(token):
            # Adicione a tarefa apenas se o token for válido
            self.c.execute('''INSERT INTO tarefas VALUES (?, ?, ?, ?, ?, ?)''',
                           (tarefa.id, tarefa.titulo, tarefa.descricao,
                            tarefa.data_inicio.strftime("%Y-%m-%d %H:%M:%S"),
                            tarefa.data_conclusao_prevista.strftime("%Y-%m-%d %H:%M:%S"),
                            tarefa.status))
            self.conn.commit()
        else:
            print("Token inválido. Operação não autorizada.")
