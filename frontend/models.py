from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_conclusao_prevista = models.DateTimeField()
    status = models.CharField(max_length=20, default="Pendente")

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'frontend'
