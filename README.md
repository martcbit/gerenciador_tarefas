## Projeto de Sistema de Gerenciamento de Tarefas

Este é um projeto de sistema de gerenciamento de tarefas com backend e frontend, onde você pode adicionar, editar, remover e listar tarefas. O backend é desenvolvido em Python utilizando SQLite como banco de dados, enquanto o frontend é uma aplicação web em Django.

### Funcionalidades

- Adicionar tarefas
- Editar tarefas
- Remover tarefas
- Listar tarefas

### Pré-requisitos

Certifique-se de ter instalado o seguinte em sua máquina:

- Python (versão 3.x)
- Django
- SQLite (ou outro banco de dados de sua escolha)

### Configuração

1. Clone o repositório para sua máquina local:
   ```
   git clone [https://github.com/martcbit/gerenciador_tarefas.git]
   ```
2. Navegue até o diretório do projeto:
   ```
   cd gerenciador_tarefas
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências do Python:
   ```
   pip install -r requirements.txt
   ```

5. Configure o banco de dados:
   - O projeto já está configurado para usar SQLite por padrão. Se desejar usar outro banco de dados, atualize as configurações em `backend/settings.py`.

6. Execute as migrações para criar as tabelas do banco de dados:
   ```
   python manage.py migrate
   ```

### Executando o Servidor

1. Inicie o servidor Django:
   ```
   python manage.py runserver
   ```

2. Acesse o sistema em seu navegador através do seguinte link:
   ```
   http://localhost:8000/
   ```
### URLs do Projeto Gerenciador de Tarefas

### Administração
* **/admin/**: URL para acessar a interface de administração do Django.
#### Criação de um Superusuário

Se você não tiver um superusuário, siga estas etapas para criar um:

1. Abra um terminal e navegue até o diretório raiz do seu projeto Django.

2. Execute o seguinte comando para criar um superusuário:

    ```
    python manage.py createsuperuser
    ```

### Frontend
* **/frontend/**: URL base para acessar as páginas do frontend.

### Páginas
* **/frontend/listar_tarefas/**: Página para listar todas as tarefas cadastradas.

### API

A API do Gerenciador de Tarefas fornece endpoints para realizar operações CRUD nas tarefas.

* **/api/adicionar_tarefa/ (POST)**: Adiciona uma nova tarefa.
    * **Parâmetros POST:**
        * titulo: Título da tarefa (obrigatório).
        * descricao: Descrição da tarefa (opcional).
        * data_inicio: Data de início da tarefa no formato YYYY-MM-DD (obrigatório).
        * data_conclusao_prevista: Data de conclusão prevista da tarefa no formato YYYY-MM-DD (obrigatório).
        * status: Status da tarefa (opcional, padrão: "Pendente").
    * **Retorna um JSON com a mensagem de sucesso ou erro.**

* **/api/listar_tarefas/ (GET)**: Lista todas as tarefas cadastradas.
    * **Retorna um JSON com a lista de todas as tarefas.**


### Testes

Para executar os testes unitários, use o seguinte comando:
   ```
   python -m unittest discover -p "test_*.py"
   ```

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para relatar um problema ou sugerir uma melhoria.

### Autores

- [Seu Nome](https://github.com/seu_usuario)

### Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
